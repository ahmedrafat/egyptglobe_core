app_name = "egyptglobe_core"
app_title = "EgyptGlobe Core"
app_publisher = "EgyptGlobe Group"
app_description = "Custom Frappe app for salt, fertilizer, machinery, and global operations"
app_icon = "octicon octicon-globe"
app_color = "blue"
app_email = "info@egyptglobe.com"
app_license = "MIT"

after_install = "egyptglobe_core.setup.setup_after_install.after_install"

fixtures = [
    "Custom Field",
    "Property Setter",
    "Print Format",
    "Client Script",
    "Report",
    "Workflow",
    "Dashboard",
    "Workspace",
    {"dt": "DocType", "filters": [["custom", "=", 1]]}
]