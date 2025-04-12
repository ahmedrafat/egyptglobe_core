import frappe
import re

def make_slug(name):
    # Custom scrub logic (similar to frappe.utils.scrub)
    return re.sub(r'\W+', '_', name.strip().lower())

def execute():
    custom_doctypes = frappe.get_all("DocType", filters={"custom": 1}, pluck="name")
    for dt in custom_doctypes:
        slug = make_slug(dt)
        if not frappe.db.exists("Page", slug):
            doc = frappe.get_doc({
                "doctype": "Page",
                "page_name": slug,
                "module": frappe.get_doc("DocType", dt).module,
                "title": dt,
                "content": "",
                "is_standard": 0
            })
            doc.insert(ignore_permissions=True)