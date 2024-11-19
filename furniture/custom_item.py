import frappe
from frappe.utils import today

from erpnext.stock.doctype.item.item import Item

def set_last_purchase_rate(self, new_name):
    last_purchase_rate = get_last_purchase_details(new_name).get("base_net_rate", 0)
    frappe.db.set_value("Item", new_name, "last_purchase_rate", last_purchase_rate)
    frappe.db.set_value("Item", new_name, "last_rate_update", today())

Item.set_last_purchase_rate = set_last_purchase_rate