import frappe

def after_install():
    modules = ['Machinery', 'Salt', 'Fertilizers', 'Logistics', 'Water Treatment', 'Grains', 'Chemicals', 'Cotton Products', 'Oil and Herbs']
    for mod in modules:
        ensure_module(mod)
    create_machinery_product()
    create_component_spec()
    create_service_history()
    create_salt_specification()
    create_salt_batch()
    create_salt_test_result()
    create_fertilizer_type()
    create_nutrient_breakdown()
    create_freight_plan()
    create_container_movement()
    create_water_quality_report()
    create_treatment_stage()
    create_grain_type()
    create_moisture_analysis()
    create_chemical_product()
    create_handling_instruction()
    create_cotton_type()
    create_ginning_record()
    create_herb_type()
    create_oil_sample()

def ensure_module(module_name):
    if not frappe.db.exists('Module Def', module_name):
        frappe.get_doc({
            'doctype': 'Module Def',
            'module_name': module_name,
            'app_name': 'egyptglobe_core'
        }).insert(ignore_permissions=True)

def create_machinery_product():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Machinery Product',
        'module': 'Machinery',
        'custom': 1,
        'fields': [
            {'label': 'Model Name', 'fieldname': 'model_name', 'fieldtype': 'Data'},
            {'label': 'Capacity', 'fieldname': 'capacity', 'fieldtype': 'Float'},
            {'label': 'Power Rating', 'fieldname': 'power_rating', 'fieldtype': 'Float'},
            {'label': 'Control System', 'fieldname': 'control_system', 'fieldtype': 'Select', 'options': 'Manual\nPLC\nHMI'},
        ]
    }).insert(ignore_permissions=True)

def create_component_spec():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Component Spec',
        'module': 'Machinery',
        'custom': 1,
        'fields': [
            {'label': 'Component Name', 'fieldname': 'component_name', 'fieldtype': 'Data'},
            {'label': 'Specification', 'fieldname': 'specification', 'fieldtype': 'Text'},
        ]
    }).insert(ignore_permissions=True)

def create_service_history():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Service History',
        'module': 'Machinery',
        'custom': 1,
        'fields': [
            {'label': 'Machinery', 'fieldname': 'machinery', 'fieldtype': 'Link', 'options': 'Machinery Product'},
            {'label': 'Service Date', 'fieldname': 'service_date', 'fieldtype': 'Date'},
            {'label': 'Notes', 'fieldname': 'notes', 'fieldtype': 'Text'},
        ]
    }).insert(ignore_permissions=True)

def create_salt_specification():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Salt Specification',
        'module': 'Salt',
        'custom': 1,
        'fields': [
            {'label': 'Salt Type', 'fieldname': 'salt_type', 'fieldtype': 'Select', 'options': 'Sea\nRock\nLake\nVacuum'},
            {'label': 'Grain Size', 'fieldname': 'grain_size', 'fieldtype': 'Data'},
            {'label': 'Purity (%)', 'fieldname': 'purity', 'fieldtype': 'Float'},
            {'label': 'Moisture (%)', 'fieldname': 'moisture', 'fieldtype': 'Float'},
            {'label': 'Iodized', 'fieldname': 'iodized', 'fieldtype': 'Check'},
        ]
    }).insert(ignore_permissions=True)

def create_salt_batch():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Salt Batch',
        'module': 'Salt',
        'custom': 1,
        'fields': [
            {'label': 'Batch No', 'fieldname': 'batch_no', 'fieldtype': 'Data'},
            {'label': 'Source', 'fieldname': 'source', 'fieldtype': 'Data'},
            {'label': 'Specification', 'fieldname': 'spec', 'fieldtype': 'Link', 'options': 'Salt Specification'},
        ]
    }).insert(ignore_permissions=True)

def create_salt_test_result():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Salt Test Result',
        'module': 'Salt',
        'custom': 1,
        'fields': [
            {'label': 'Batch', 'fieldname': 'batch', 'fieldtype': 'Link', 'options': 'Salt Batch'},
            {'label': 'Purity', 'fieldname': 'purity', 'fieldtype': 'Float'},
            {'label': 'Moisture', 'fieldname': 'moisture', 'fieldtype': 'Float'},
            {'label': 'Comments', 'fieldname': 'comments', 'fieldtype': 'Text'},
        ]
    }).insert(ignore_permissions=True)

def create_fertilizer_type():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Fertilizer Type',
        'module': 'Fertilizers',
        'custom': 1,
        'fields': [
            {'label': 'Product Name', 'fieldname': 'product_name', 'fieldtype': 'Data'},
            {'label': 'N-P-K Ratio', 'fieldname': 'npk_ratio', 'fieldtype': 'Data'},
            {'label': 'Granular or Powder', 'fieldname': 'form', 'fieldtype': 'Select', 'options': 'Granular\nPowder\nLiquid'},
        ]
    }).insert(ignore_permissions=True)

def create_nutrient_breakdown():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Nutrient Breakdown',
        'module': 'Fertilizers',
        'custom': 1,
        'fields': [
            {'label': 'Fertilizer', 'fieldname': 'fertilizer', 'fieldtype': 'Link', 'options': 'Fertilizer Type'},
            {'label': 'Nitrogen %', 'fieldname': 'nitrogen', 'fieldtype': 'Float'},
            {'label': 'Phosphorus %', 'fieldname': 'phosphorus', 'fieldtype': 'Float'},
            {'label': 'Potassium %', 'fieldname': 'potassium', 'fieldtype': 'Float'},
        ]
    }).insert(ignore_permissions=True)

def create_freight_plan():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Freight Plan',
        'module': 'Logistics',
        'custom': 1,
        'fields': [
            {'label': 'Port of Loading', 'fieldname': 'pol', 'fieldtype': 'Data'},
            {'label': 'Port of Discharge', 'fieldname': 'pod', 'fieldtype': 'Data'},
            {'label': 'Vessel Name', 'fieldname': 'vessel_name', 'fieldtype': 'Data'},
            {'label': 'ETD', 'fieldname': 'etd', 'fieldtype': 'Date'},
            {'label': 'ETA', 'fieldname': 'eta', 'fieldtype': 'Date'},
        ]
    }).insert(ignore_permissions=True)

def create_container_movement():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Container Movement',
        'module': 'Logistics',
        'custom': 1,
        'fields': [
            {'label': 'Container No', 'fieldname': 'container_no', 'fieldtype': 'Data'},
            {'label': 'Movement Type', 'fieldname': 'movement_type', 'fieldtype': 'Select', 'options': 'In\nOut\nTransfer'},
            {'label': 'Date', 'fieldname': 'movement_date', 'fieldtype': 'Date'},
        ]
    }).insert(ignore_permissions=True)

def create_water_quality_report():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Water Quality Report',
        'module': 'Water Treatment',
        'custom': 1,
        'fields': [
            {'label': 'Sample Source', 'fieldname': 'source', 'fieldtype': 'Data'},
            {'label': 'pH Level', 'fieldname': 'ph', 'fieldtype': 'Float'},
            {'label': 'TDS (ppm)', 'fieldname': 'tds', 'fieldtype': 'Float'},
            {'label': 'Conductivity', 'fieldname': 'conductivity', 'fieldtype': 'Float'},
        ]
    }).insert(ignore_permissions=True)

def create_treatment_stage():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Treatment Stage',
        'module': 'Water Treatment',
        'custom': 1,
        'fields': [
            {'label': 'Stage Name', 'fieldname': 'stage_name', 'fieldtype': 'Data'},
            {'label': 'Purpose', 'fieldname': 'purpose', 'fieldtype': 'Text'},
        ]
    }).insert(ignore_permissions=True)

def create_grain_type():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Grain Type',
        'module': 'Grains',
        'custom': 1,
        'fields': [
            {'label': 'Grain Name', 'fieldname': 'grain_name', 'fieldtype': 'Data'},
            {'label': 'Origin', 'fieldname': 'origin', 'fieldtype': 'Data'},
            {'label': 'Grade', 'fieldname': 'grade', 'fieldtype': 'Select', 'options': 'A\nB\nC'},
        ]
    }).insert(ignore_permissions=True)

def create_moisture_analysis():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Moisture Analysis',
        'module': 'Grains',
        'custom': 1,
        'fields': [
            {'label': 'Grain Type', 'fieldname': 'grain_type', 'fieldtype': 'Link', 'options': 'Grain Type'},
            {'label': 'Moisture Level', 'fieldname': 'moisture_level', 'fieldtype': 'Float'},
            {'label': 'Date Tested', 'fieldname': 'date_tested', 'fieldtype': 'Date'},
        ]
    }).insert(ignore_permissions=True)

def create_chemical_product():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Chemical Product',
        'module': 'Chemicals',
        'custom': 1,
        'fields': [
            {'label': 'Product Name', 'fieldname': 'product_name', 'fieldtype': 'Data'},
            {'label': 'CAS Number', 'fieldname': 'cas_number', 'fieldtype': 'Data'},
            {'label': 'Form', 'fieldname': 'form', 'fieldtype': 'Select', 'options': 'Liquid\nSolid\nGas'},
        ]
    }).insert(ignore_permissions=True)

def create_handling_instruction():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Handling Instruction',
        'module': 'Chemicals',
        'custom': 1,
        'fields': [
            {'label': 'Chemical', 'fieldname': 'chemical', 'fieldtype': 'Link', 'options': 'Chemical Product'},
            {'label': 'Safety Instruction', 'fieldname': 'instruction', 'fieldtype': 'Text'},
        ]
    }).insert(ignore_permissions=True)

def create_cotton_type():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Cotton Type',
        'module': 'Cotton Products',
        'custom': 1,
        'fields': [
            {'label': 'Type', 'fieldname': 'type', 'fieldtype': 'Data'},
            {'label': 'Length (mm)', 'fieldname': 'length', 'fieldtype': 'Float'},
            {'label': 'Strength', 'fieldname': 'strength', 'fieldtype': 'Float'},
        ]
    }).insert(ignore_permissions=True)

def create_ginning_record():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Ginning Record',
        'module': 'Cotton Products',
        'custom': 1,
        'fields': [
            {'label': 'Batch No', 'fieldname': 'batch_no', 'fieldtype': 'Data'},
            {'label': 'Cotton Type', 'fieldname': 'cotton_type', 'fieldtype': 'Link', 'options': 'Cotton Type'},
            {'label': 'Ginned Date', 'fieldname': 'ginned_date', 'fieldtype': 'Date'},
        ]
    }).insert(ignore_permissions=True)

def create_herb_type():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Herb Type',
        'module': 'Oil and Herbs',
        'custom': 1,
        'fields': [
            {'label': 'Herb Name', 'fieldname': 'herb_name', 'fieldtype': 'Data'},
            {'label': 'Part Used', 'fieldname': 'part_used', 'fieldtype': 'Select', 'options': 'Leaf\nRoot\nFlower\nSeed'},
        ]
    }).insert(ignore_permissions=True)

def create_oil_sample():
    frappe.get_doc({
        'doctype': 'DocType',
        'name': 'Oil Sample',
        'module': 'Oil and Herbs',
        'custom': 1,
        'fields': [
            {'label': 'Herb', 'fieldname': 'herb', 'fieldtype': 'Link', 'options': 'Herb Type'},
            {'label': 'Purity (%)', 'fieldname': 'purity', 'fieldtype': 'Float'},
            {'label': 'Extraction Method', 'fieldname': 'extraction_method', 'fieldtype': 'Data'},
        ]
    }).insert(ignore_permissions=True)
