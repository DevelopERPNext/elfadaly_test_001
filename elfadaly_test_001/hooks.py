app_name = "elfadaly_test_001"
app_title = "Elfadaly Test 001"
app_publisher = "khattab.info"
app_description = "Elfadaly Test 001"
app_email = "khattab@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------




app_include_css = "/assets/elfadaly_test_001/css/workspace.css"




doctype_js = {
    "Purchase Order": "public/js/custom_js.js",
    "Purchase Invoice": "public/js/custom_js.js",
    "Sales Order": "public/js/custom_js.js",
    "Sales Invoice": "public/js/custom_js.js",
    "Purchase Receipt": "public/js/custom_js.js",
    "Delivery Note": "public/js/custom_js.js",
    "Stock Entry": "public/js/custom_js.js",
    "Work Order": "public/js/custom_js.js",
    "BOM": "public/js/custom_js.js",
    "Workstation": "public/js/custom_js.js",
    "Routing": "public/js/custom_js.js",
    "Item": "public/js/custom_js.js",
    "POS Invoice": "public/js/custom_js.js",
}


doctype_list_js = {
    "Purchase Order": "public/js/custom_js.js",
    "Purchase Invoice": "public/js/custom_js.js",
    "Sales Order": "public/js/custom_js.js",
    "Sales Invoice": "public/js/custom_js.js",
    "Purchase Receipt": "public/js/custom_js.js",
    "Delivery Note": "public/js/custom_js.js",
    "Stock Entry": "public/js/custom_js.js",
}




# ================  Adding ========================



# override_doctype_class = {
#     "Work Order": "elfadaly_test_001.overrides.work_order.CustomWorkOrder",
# }

doc_events = {
    "Stock Entry": {
        # "validate": [
        "before_submit": [
            # "elfadaly_test_001.elfadaly_test_001.custom.create_print_msg",
            "elfadaly_test_001.elfadaly_test_001.custom.before_submit_branch",
        ],
        # "validate": [
        #     "elfadaly_test_001.elfadaly_test_001.custom.fetch_qty_from_table_scrap_item_in_bom",
        #     # "elfadaly_test_001.elfadaly_test_001.custom.fetch_bom_check_a_001",
        # ],
    },
    # "Work Order": {
    #     "validate": [
    #         # "elfadaly_test_001.elfadaly_test_001.custom.mod_qty",
    #     ]
    # }
}





fixtures = [{"dt": "Custom Field", "filters": [["module", "=", "Elfadaly Test 001"]]}]




# include js, css files in header of desk.html
# app_include_css = "/assets/elfadaly_test_001/css/elfadaly_test_001.css"
# app_include_js = "/assets/elfadaly_test_001/js/elfadaly_test_001.js"

# include js, css files in header of web template
# web_include_css = "/assets/elfadaly_test_001/css/elfadaly_test_001.css"
# web_include_js = "/assets/elfadaly_test_001/js/elfadaly_test_001.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "elfadaly_test_001/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "elfadaly_test_001/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "elfadaly_test_001.utils.jinja_methods",
# 	"filters": "elfadaly_test_001.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "elfadaly_test_001.install.before_install"
# after_install = "elfadaly_test_001.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "elfadaly_test_001.uninstall.before_uninstall"
# after_uninstall = "elfadaly_test_001.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "elfadaly_test_001.utils.before_app_install"
# after_app_install = "elfadaly_test_001.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "elfadaly_test_001.utils.before_app_uninstall"
# after_app_uninstall = "elfadaly_test_001.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "elfadaly_test_001.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"elfadaly_test_001.tasks.all"
# 	],
# 	"daily": [
# 		"elfadaly_test_001.tasks.daily"
# 	],
# 	"hourly": [
# 		"elfadaly_test_001.tasks.hourly"
# 	],
# 	"weekly": [
# 		"elfadaly_test_001.tasks.weekly"
# 	],
# 	"monthly": [
# 		"elfadaly_test_001.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "elfadaly_test_001.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "elfadaly_test_001.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "elfadaly_test_001.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["elfadaly_test_001.utils.before_request"]
# after_request = ["elfadaly_test_001.utils.after_request"]

# Job Events
# ----------
# before_job = ["elfadaly_test_001.utils.before_job"]
# after_job = ["elfadaly_test_001.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"elfadaly_test_001.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

