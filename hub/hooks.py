app_name = "hub"
app_title = "Hub"
app_publisher = "Frappe"
app_description = "ERPNext Commerce Hub"
app_icon = "octicon octicon-database"
app_color = "#4a4a4a"
app_email = "info@frappe.io"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hub/css/hub.css"
# app_include_js = "/assets/hub/js/hub.js"

# include js, css files in header of web template
# web_include_css = "/assets/hub/css/hub.css"
# web_include_js = "/assets/hub/js/hub.js"

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

# Installation
# ------------

# before_install = "hub.install.before_install"
# after_install = "hub.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hub.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hub.tasks.all"
# 	],
# 	"daily": [
# 		"hub.tasks.daily"
# 	],
# 	"hourly": [
# 		"hub.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hub.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hub.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hub.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hub.event.get_events"
# }

