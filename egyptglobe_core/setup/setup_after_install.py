import frappe

def after_install():
    # Install all required base data and create sample DocTypes if not already created

    # Example: Create Machinery Category
    if not frappe.db.exists("DocType", "Machinery Product"):
        create_machinery_product()

    if not frappe.db.exists("DocType", "COA"):
        create_coa()

    if not frappe.db.exists("DocType", "Salt Product Spec"):
        create_salt_product_spec()

def create_machinery_product():
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Machinery Product",
        "module": "Machinery",
        "custom": 1,
        "fields": [
            {"label": "Model Name", "fieldname": "model_name", "fieldtype": "Data", "reqd": 1},
            {"label": "Capacity", "fieldname": "capacity", "fieldtype": "Float"},
            {"label": "Power Rating", "fieldname": "power_rating", "fieldtype": "Float"},
            {"label": "Control System", "fieldname": "control_system", "fieldtype": "Select", "options": "Manual\nPLC\nHMI"},
            {"label": "CAD Drawing Ref", "fieldname": "cad_drawing_ref", "fieldtype": "Attach"}
        ]
    })
    doc.insert(ignore_permissions=True)

def create_coa():
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "COA",
        "module": "Compliance",
        "custom": 1,
        "fields": [
            {"label": "Product", "fieldname": "product", "fieldtype": "Link", "options": "Item", "reqd": 1},
            {"label": "Batch No", "fieldname": "batch_no", "fieldtype": "Data", "reqd": 1},
            {"label": "Test Results", "fieldname": "test_results", "fieldtype": "Table", "options": "COA Test Result"},
            {"label": "Issued By", "fieldname": "issued_by", "fieldtype": "Link", "options": "User"},
            {"label": "ILAC Certified", "fieldname": "ilac_certified", "fieldtype": "Check"}
        ]
    })
    doc.insert(ignore_permissions=True)

def create_salt_product_spec():
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Salt Product Spec",
        "module": "Salt",
        "custom": 1,
        "fields": [
            {"label": "Salt Type", "fieldname": "salt_type", "fieldtype": "Select", "options": "Rock\nSea\nLake\nVacuum"},
            {"label": "Grain Size", "fieldname": "grain_size", "fieldtype": "Data"},
            {"label": "Moisture", "fieldname": "moisture", "fieldtype": "Percent"},
            {"label": "Purity", "fieldname": "purity", "fieldtype": "Percent"},
            {"label": "Iodized", "fieldname": "iodized", "fieldtype": "Check"}
        ]
    })
    doc.insert(ignore_permissions=True)