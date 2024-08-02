app_name = "subscription_app"
app_title = "Subscription App"
app_publisher = "khayam khan"
app_description = "A Small Frappe App for BOT Solutions to manage Subscriptions of Customers"
app_email = "khayamkhan852@gmail.com"
app_license = "mit"
# required_apps = []

fixtures = [
    "Email Template"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/subscription_app/css/subscription_app.css"
# app_include_js = "/assets/subscription_app/js/subscription_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/subscription_app/css/subscription_app.css"
# web_include_js = "/assets/subscription_app/js/subscription_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "subscription_app/public/scss/website"

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
# app_include_icons = "subscription_app/public/icons.svg"

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
# 	"methods": "subscription_app.utils.jinja_methods",
# 	"filters": "subscription_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "subscription_app.install.before_install"
# after_install = "subscription_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "subscription_app.uninstall.before_uninstall"
# after_uninstall = "subscription_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "subscription_app.utils.before_app_install"
# after_app_install = "subscription_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "subscription_app.utils.before_app_uninstall"
# after_app_uninstall = "subscription_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "subscription_app.notifications.get_notification_config"

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

scheduler_events = {
	# "all": [
	# 	"subscription_app.tasks.all"
	# ],
	"daily": [
		"subscription_app.subscription_app.doctype.bot_subscription.bot_subscription.send_reminder_emails"
	],
	# "hourly": [
	# 	"subscription_app.tasks.hourly"
	# ],
	# "weekly": [
	# 	"subscription_app.tasks.weekly"
	# ],
	# "monthly": [
	# 	"subscription_app.tasks.monthly"
	# ],
}

# Testing
# -------

# before_tests = "subscription_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "subscription_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "subscription_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["subscription_app.utils.before_request"]
# after_request = ["subscription_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["subscription_app.utils.before_job"]
# after_job = ["subscription_app.utils.after_job"]

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
# 	"subscription_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

