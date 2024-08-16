# Copyright (c) 2024, khattab.info and contributors
# For license information, please see license.txt

import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data




# =================================================
# def execute(filters=None):
#     columns = [
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 120},
#     ]
#
#     data = frappe.db.sql("""
#         SELECT
#             op.operation AS operation,
#             op.workstation AS workstation,
#             op.planned_operating_cost AS planned_operating_cost,
#             op.actual_operating_cost AS actual_operating_cost,
#             (op.actual_operating_cost - op.planned_operating_cost) AS cost_difference,
#             op.time_in_mins AS planned_operation_time,
#             op.actual_operation_time AS actual_operation_time,
#             (op.actual_operation_time - op.time_in_mins) AS time_difference,
#             op.status AS operation_status
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         WHERE wo.docstatus = 1
#     """, as_dict=1)
#
#     return columns, data



# =================================================
# def execute(filters=None):
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "work_order_total", "label": "Work Order Total (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float",
#          "width": 150},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float",
#          "width": 150},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 120},
#     ]
#
#     # Fetch work orders and their operations
#     work_orders = frappe.db.sql("""
#         SELECT
#             wo.name AS work_order,
#             wo.total_operating_cost AS work_order_total,
#             op.operation AS operation,
#             op.workstation AS workstation,
#             op.planned_operating_cost AS planned_operating_cost,
#             op.actual_operating_cost AS actual_operating_cost,
#             (op.actual_operating_cost - op.planned_operating_cost) AS cost_difference,
#             op.time_in_mins AS planned_operation_time,
#             op.actual_operation_time AS actual_operation_time,
#             (op.actual_operation_time - op.time_in_mins) AS time_difference,
#             op.status AS operation_status
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         WHERE wo.docstatus = 1
#         ORDER BY wo.name, op.operation
#     """, as_dict=1)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         # Insert a new row for the Work Order if it's different from the last one
#         if row['work_order'] != current_work_order:
#             data.append({
#                 "work_order": row['work_order'],
#                 "work_order_total": row['work_order_total'],
#                 "operation": None,
#                 "workstation": None,
#                 "planned_operating_cost": None,
#                 "actual_operating_cost": None,
#                 "cost_difference": None,
#                 "planned_operation_time": None,
#                 "actual_operation_time": None,
#                 "time_difference": None,
#                 "operation_status": None,
#             })
#             current_work_order = row['work_order']
#
#         # Add the operation details
#         data.append({
#             "work_order": None,  # Keep this blank for operations rows
#             "work_order_total": None,  # Keep this blank for operations rows
#             "operation": row['operation'],
#             "workstation": row['workstation'],
#             "planned_operating_cost": row['planned_operating_cost'],
#             "actual_operating_cost": row['actual_operating_cost'],
#             "cost_difference": row['cost_difference'],
#             "planned_operation_time": row['planned_operation_time'],
#             "actual_operation_time": row['actual_operation_time'],
#             "time_difference": row['time_difference'],
#             "operation_status": row['operation_status'],
#         })
#
#     return columns, data

















# =================================================

#
#
# def execute(filters=None):
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)",
#          "fieldtype": "Currency", "width": 150},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency",
#          "width": 150},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float",
#          "width": 150},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float",
#          "width": 150},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 120},
#     ]
#
#     # Fetch work orders and their operations
#     work_orders = frappe.db.sql("""
#         SELECT
#             wo.name AS work_order,
#             wo.total_operating_cost AS actual_work_order_total,
#             wo.planned_operating_cost AS planned_work_order_total,
#             (wo.total_operating_cost - wo.planned_operating_cost) AS work_order_difference,
#             op.operation AS operation,
#             op.workstation AS workstation,
#             op.planned_operating_cost AS planned_operating_cost,
#             op.actual_operating_cost AS actual_operating_cost,
#             (op.actual_operating_cost - op.planned_operating_cost) AS cost_difference,
#             op.time_in_mins AS planned_operation_time,
#             op.actual_operation_time AS actual_operation_time,
#             (op.actual_operation_time - op.time_in_mins) AS time_difference,
#             op.status AS operation_status
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         WHERE wo.docstatus = 1
#         ORDER BY wo.name, op.operation
#     """, as_dict=1)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         # Insert a new row for the Work Order if it's different from the last one
#         if row['work_order'] != current_work_order:
#             data.append({
#                 "work_order": row['work_order'],
#                 "planned_work_order_total": row['planned_work_order_total'],
#                 "actual_work_order_total": row['actual_work_order_total'],
#                 "work_order_difference": row['work_order_difference'],
#                 "operation": None,
#                 "workstation": None,
#                 "planned_operating_cost": None,
#                 "actual_operating_cost": None,
#                 "cost_difference": None,
#                 "planned_operation_time": None,
#                 "actual_operation_time": None,
#                 "time_difference": None,
#                 "operation_status": None,
#             })
#             current_work_order = row['work_order']
#
#         # Add the operation details
#         data.append({
#             "work_order": None,  # Keep this blank for operations rows
#             "planned_work_order_total": None,  # Keep this blank for operations rows
#             "actual_work_order_total": None,  # Keep this blank for operations rows
#             "work_order_difference": None,  # Keep this blank for operations rows
#             "operation": row['operation'],
#             "workstation": row['workstation'],
#             "planned_operating_cost": row['planned_operating_cost'],
#             "actual_operating_cost": row['actual_operating_cost'],
#             "cost_difference": row['cost_difference'],
#             "planned_operation_time": row['planned_operation_time'],
#             "actual_operation_time": row['actual_operation_time'],
#             "time_difference": row['time_difference'],
#             "operation_status": row['operation_status'],
#         })
#
#     return columns, data








# =================================================


#
#
# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 150},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 120},
#     ]
#
#     conditions = ""
#     if filters.get("work_order"):
#         conditions += "AND wo.name = %(work_order)s "
#     if filters.get("item_code"):
#         conditions += "AND wo.production_item = %(item_code)s "
#
#     work_orders = frappe.db.sql(f"""
#         SELECT
#             wo.name AS work_order,
#             wo.production_item AS item_code,
#             wo.total_operating_cost AS actual_work_order_total,
#             wo.planned_operating_cost AS planned_work_order_total,
#             (wo.total_operating_cost - wo.planned_operating_cost) AS work_order_difference,
#             op.operation AS operation,
#             op.workstation AS workstation,
#             op.planned_operating_cost AS planned_operating_cost,
#             op.actual_operating_cost AS actual_operating_cost,
#             (op.actual_operating_cost - op.planned_operating_cost) AS cost_difference,
#             op.time_in_mins AS planned_operation_time,
#             op.actual_operation_time AS actual_operation_time,
#             (op.actual_operation_time - op.time_in_mins) AS time_difference,
#             op.status AS operation_status
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         WHERE wo.docstatus = 1 {conditions}
#         ORDER BY wo.name, op.operation
#     """, filters, as_dict=1)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         if row['work_order'] != current_work_order:
#             data.append({
#                 "work_order": row['work_order'],
#                 "item_code": row['item_code'],
#                 "planned_work_order_total": row['planned_work_order_total'],
#                 "actual_work_order_total": row['actual_work_order_total'],
#                 "work_order_difference": row['work_order_difference'],
#                 "operation": None,
#                 "workstation": None,
#                 "planned_operating_cost": None,
#                 "actual_operating_cost": None,
#                 "cost_difference": None,
#                 "planned_operation_time": None,
#                 "actual_operation_time": None,
#                 "time_difference": None,
#                 "operation_status": None,
#             })
#             current_work_order = row['work_order']
#
#         data.append({
#             "work_order": None,
#             "item_code": None,
#             "planned_work_order_total": None,
#             "actual_work_order_total": None,
#             "work_order_difference": None,
#             "operation": row['operation'],
#             "workstation": row['workstation'],
#             "planned_operating_cost": row['planned_operating_cost'],
#             "actual_operating_cost": row['actual_operating_cost'],
#             "cost_difference": row['cost_difference'],
#             "planned_operation_time": row['planned_operation_time'],
#             "actual_operation_time": row['actual_operation_time'],
#             "time_difference": row['time_difference'],
#             "operation_status": row['operation_status'],
#         })
#
#     return columns, data
#








# =================================================







def execute(filters=None):
    if not filters:
        filters = {}

    columns = [
        {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
        {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
        {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 150},
        {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 200},
        {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 150},
        {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 150},
        {"fieldname": "qty_difference", "label": "Difference (Process Loss)", "fieldtype": "Float", "width": 150},
        {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 150},
        {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 150},
        {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
        {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
        {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
        {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 150},
        {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 150},
        {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 150},
        {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 150},
        {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 150},
        {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 150},
        {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 120},
    ]

    conditions = ""
    if filters.get("work_order"):
        conditions += "AND wo.name = %(work_order)s "
    if filters.get("item_code"):
        conditions += "AND wo.production_item = %(item_code)s "

    work_orders = frappe.db.sql(f"""
        SELECT 
            wo.name AS work_order,
            wo.production_item AS item_code,
            wo.qty AS qty_to_manufacture,
            wo.material_transferred_for_manufacturing AS material_transferred,
            wo.produced_qty AS manufactured_qty,
            (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
            wo.total_operating_cost AS actual_work_order_total,
            wo.planned_operating_cost AS planned_work_order_total,
            (wo.total_operating_cost - wo.planned_operating_cost) AS work_order_difference,
            op.operation AS operation,
            op.workstation AS workstation,
            op.planned_operating_cost AS planned_operating_cost,
            op.actual_operating_cost AS actual_operating_cost,
            (op.actual_operating_cost - op.planned_operating_cost) AS cost_difference,
            op.time_in_mins AS planned_operation_time,
            op.actual_operation_time AS actual_operation_time,
            (op.actual_operation_time - op.time_in_mins) AS time_difference,
            op.status AS operation_status
        FROM `tabWork Order` wo
        JOIN `tabWork Order Operation` op ON wo.name = op.parent
        WHERE wo.docstatus = 1 {conditions}
        ORDER BY wo.name, op.operation
    """, filters, as_dict=1)

    data = []
    current_work_order = None

    for row in work_orders:
        if row['work_order'] != current_work_order:
            data.append({
                "work_order": row['work_order'],
                "item_code": row['item_code'],
                "qty_to_manufacture": row['qty_to_manufacture'],
                "material_transferred": row['material_transferred'],
                "manufactured_qty": row['manufactured_qty'],
                "process_loss_qty": row['process_loss_qty'],
                "qty_difference": row['process_loss_qty'],  # If there's a specific formula for this, adjust here
                "planned_work_order_total": row['planned_work_order_total'],
                "actual_work_order_total": row['actual_work_order_total'],
                "work_order_difference": row['work_order_difference'],
                "operation": None,
                "workstation": None,
                "planned_operating_cost": None,
                "actual_operating_cost": None,
                "cost_difference": None,
                "planned_operation_time": None,
                "actual_operation_time": None,
                "time_difference": None,
                "operation_status": None,
            })
            current_work_order = row['work_order']

        data.append({
            "work_order": None,
            "item_code": None,
            "qty_to_manufacture": None,
            "material_transferred": None,
            "manufactured_qty": None,
            "process_loss_qty": None,
            "qty_difference": None,
            "planned_work_order_total": None,
            "actual_work_order_total": None,
            "work_order_difference": None,
            "operation": row['operation'],
            "workstation": row['workstation'],
            "planned_operating_cost": row['planned_operating_cost'],
            "actual_operating_cost": row['actual_operating_cost'],
            "cost_difference": row['cost_difference'],
            "planned_operation_time": row['planned_operation_time'],
            "actual_operation_time": row['actual_operation_time'],
            "time_difference": row['time_difference'],
            "operation_status": row['operation_status'],
        })

    return columns, data













