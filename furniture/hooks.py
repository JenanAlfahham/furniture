from . import __version__ as app_version

app_name = "furniture"
app_title = "Furniture"
app_publisher = "Jenan Alfahham"
app_description = "Furniture App"
app_email = "jenan_95@hotmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/furniture/css/furniture.css"
# app_include_js = "/assets/furniture/js/furniture.js"

# include js, css files in header of web template
# web_include_css = "/assets/furniture/css/furniture.css"
# web_include_js = "/assets/furniture/js/furniture.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "furniture/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "furniture.utils.jinja_methods",
#	"filters": "furniture.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "furniture.install.before_install"
# after_install = "furniture.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "furniture.uninstall.before_uninstall"
# after_uninstall = "furniture.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "furniture.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"furniture.tasks.all"
#	],
#	"daily": [
#		"furniture.tasks.daily"
#	],
#	"hourly": [
#		"furniture.tasks.hourly"
#	],
#	"weekly": [
#		"furniture.tasks.weekly"
#	],
#	"monthly": [
#		"furniture.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "furniture.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "furniture.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "furniture.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["furniture.utils.before_request"]
# after_request = ["furniture.utils.after_request"]

# Job Events
# ----------
# before_job = ["furniture.utils.before_job"]
# after_job = ["furniture.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"furniture.auth.validate"
# ]
