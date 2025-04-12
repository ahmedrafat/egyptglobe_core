import re
import frappe

def scrub(text):
    """
    Replace non-alphanumeric characters with underscores and convert to lowercase.
    Fallback scrub function if frappe.utils.scrub is unavailable.
    """
    return re.sub(r'\W+', '_', text.strip().lower())

def execute():
    custom_doctypes = frappe.get_all("DocType", filters={"custom": 1}, pluck="name")

    for dt in custom_doctypes:
        page_name = scrub(dt)
        if not frappe.db.exists("Page", page_name):
            doctype_doc = frappe.get_doc("DocType", dt)
            page = frappe.get_doc({
                "doctype": "Page",
                "page_name": page_name,
                "module": doctype_doc.module or "Core",
                "title": dt,
                "content": "",
                "is_standard": 0
            })
            page.insert(ignore_permissions=True)
            frappe.db.commit()