import frappe
from frappe.utils.nestedset import scrub
def create_pages_for_custom_doctypes():
    custom_doctypes = frappe.get_all("DocType", filters={"custom": 1}, pluck="name")
    for dt in custom_doctypes:
        route = f"app/{scrub(dt)}"
        if not frappe.db.exists("Page", {"route": route}):
            frappe.get_doc({
                "doctype": "Page",
                "title": dt,
                "module": frappe.get_value("DocType", dt, "module"),
                "name": scrub(dt),
                "route": route,
                "reference_doctype": dt,
                "standard": "Yes"
            }).insert(ignore_permissions=True)
    frappe.db.commit()