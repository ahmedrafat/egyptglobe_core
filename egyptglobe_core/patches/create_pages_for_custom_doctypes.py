import frappe
from frappe.utils.string_utils import scrub

def execute():
    custom_doctypes = frappe.get_all("DocType", filters={"custom": 1}, pluck="name")
    for dt in custom_doctypes:
        if not frappe.db.exists("Page", scrub(dt)):
            frappe.get_doc({
                "doctype": "Page",
                "page_name": scrub(dt),
                "module": frappe.get_doc("DocType", dt).module,
                "title": dt,
                "content": "",
                "is_standard": 0
            }).insert(ignore_permissions=True)