import frappe
from frappe.utils import today, getdate, flt

from erpnext.controllers.buying_controller import BuyingController
from erpnext.stock.doctype.item.item import get_last_purchase_details


def on_submit(self):
    if self.get("is_return"):
        return

    if self.doctype in ["Purchase Receipt", "Purchase Invoice"]:
        field = "purchase_invoice" if self.doctype == "Purchase Invoice" else "purchase_receipt"

        self.process_fixed_asset()
        self.update_fixed_asset(field)

    if self.doctype in ["Purchase Order", "Purchase Receipt"] and not frappe.db.get_single_value(
        "Buying Settings", "disable_last_purchase_rate"
    ):
        update_last_purchase_rate(self, is_submit=1)


def on_cancel(self):
    super(BuyingController, self).on_cancel()

    if self.get("is_return"):
        return

    if self.doctype in ["Purchase Order", "Purchase Receipt"] and not frappe.db.get_single_value(
        "Buying Settings", "disable_last_purchase_rate"
    ):
        update_last_purchase_rate(self, is_submit=0)

    if self.doctype in ["Purchase Receipt", "Purchase Invoice"]:
        field = "purchase_invoice" if self.doctype == "Purchase Invoice" else "purchase_receipt"

        self.delete_linked_asset()
        self.update_fixed_asset(field, delete_asset=True)


def update_last_purchase_rate(doc, is_submit) -> None:
    """updates last_purchase_rate and last_rate_update in item table for each item"""

    this_purchase_date = getdate(doc.get("posting_date") or doc.get("transaction_date"))

    for d in doc.get("items"):
        # get last purchase details
        last_purchase_details = get_last_purchase_details(d.item_code, doc.name)

        # compare last purchase date and this transaction's date
        last_purchase_rate = None
        if last_purchase_details and (
            doc.get("docstatus") == 2 or last_purchase_details.purchase_date > this_purchase_date
        ):
            last_purchase_rate = last_purchase_details["base_net_rate"]
        elif is_submit == 1:
            # even if this transaction is the latest one, it should be submitted
            # for it to be considered for latest purchase rate
            if flt(d.conversion_factor):
                last_purchase_rate = flt(d.base_net_rate) / flt(d.conversion_factor)
            # Check if item code is present
            # Conversion factor should not be mandatory for non itemized items
            elif d.item_code:
                frappe.throw(_("UOM Conversion factor is required in row {0}").format(d.idx))

        # update last purchsae rate
        frappe.db.set_value("Item", d.item_code, "last_purchase_rate", flt(last_purchase_rate))
        frappe.db.set_value("Item", d.item_code, "last_rate_update", today())


BuyingController.on_submit = on_submit
BuyingController.on_cancel = on_cancel

@frappe.whitelist()
def update_child_qty_rate(parent_doctype, trans_items, parent_doctype_name, child_docname="items"):
    from erpnext.controllers.accounts_controller import update_child_qty_rate

    update_child_qty_rate(parent_doctype, trans_items, parent_doctype_name, child_docname)
    if parent_doctype == "Purchase Order":
        update_last_purchase_rate(parent, is_submit=1)