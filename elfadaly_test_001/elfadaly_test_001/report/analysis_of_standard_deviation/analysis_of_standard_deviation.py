# Copyright (c) 2024, khattab.info and contributors
# For license information, please see license.txt

import frappe

import json



# # ================================================================




# ------------------------------------------------------------------
# ------------------------------------------------------------------

# # ===============  Working 001  =====================


# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 150},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 200},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 150},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 150},
#         {"fieldname": "qty_difference", "label": "Difference (Process Loss)", "fieldtype": "Float", "width": 150},
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
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
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
#                 "qty_to_manufacture": row['qty_to_manufacture'],
#                 "material_transferred": row['material_transferred'],
#                 "manufactured_qty": row['manufactured_qty'],
#                 "process_loss_qty": row['process_loss_qty'],
#                 "qty_difference": row['process_loss_qty'],
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
#             "qty_to_manufacture": None,
#             "material_transferred": None,
#             "manufactured_qty": None,
#             "process_loss_qty": None,
#             "qty_difference": None,
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






# ------------------------------------------------------------------
# ------------------------------------------------------------------







# ================================================================













# ================================================================









# ================================================================





#
# # ================================================================
#
#
#
#
# #  --------------------------------------------------------------
#
#
#
# # ===============  Working 002  =====================

#
#
#
#
# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
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
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         WHERE wo.docstatus = 1 {conditions}
#         ORDER BY wo.name, op.operation
#     """, filters, as_dict=1)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         row['process_loss_percentage'] = f"{row['process_loss_percentage']:.2f}%"
#         row['bom_process_loss_percentage'] = f"{row['bom_process_loss_percentage']:.2f}%"
#         row['process_loss_difference'] = f"{row['process_loss_difference']:.2f}%"
#
#         if row['work_order'] != current_work_order:
#             data.append({
#                 "work_order": row['work_order'],
#                 "item_code": row['item_code'],
#                 "qty_to_manufacture": row['qty_to_manufacture'],
#                 "material_transferred": row['material_transferred'],
#                 "manufactured_qty": row['manufactured_qty'],
#                 "process_loss_qty": row['process_loss_qty'],
#                 "process_loss_percentage": row['process_loss_percentage'],
#                 "bom_process_loss_percentage": row['bom_process_loss_percentage'],
#                 "process_loss_difference": row['process_loss_difference'],
#                 "process_loss_difference_qty": row['process_loss_difference_qty'],
#                 "total_finished_goods": row['total_finished_goods'],
#                 "bom_link": row.get('bom_link', 'N/A'),
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
#             "qty_to_manufacture": None,
#             "material_transferred": None,
#             "manufactured_qty": None,
#             "process_loss_qty": None,
#             "process_loss_percentage": None,
#             "bom_process_loss_percentage": None,
#             "process_loss_difference": None,
#             "process_loss_difference_qty": None,
#             "total_finished_goods": None,
#             "bom_link": None,
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









# ================================================================




#  --------------------------------------------------------------





# ================================================================
# ================================================================





# # ===============  Working 003  =====================














#
#
# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
#         {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "planned_qty_for_operation", "label": "Planned Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "actual_qty_for_operation", "label": "Actual Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "qty_difference", "label": "Qty Difference", "fieldtype": "Float", "width": 200},
#         {"fieldname": "planned_cost_per_operation", "label": "Planned Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_cost_per_operation", "label": "Actual Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
#             item.item_name AS product_name,
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#             op.status AS operation_status,
#             (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
#
#             (CASE WHEN op.planned_operating_cost > 0 THEN (op.planned_operating_cost / op.time_in_mins) ELSE 0 END) AS planned_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
#         WHERE wo.docstatus = 1 {conditions}
#         ORDER BY wo.name, op.operation
#     """, filters, as_dict=1)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         row['process_loss_percentage'] = f"{row['process_loss_percentage']:.2f}%"
#         row['bom_process_loss_percentage'] = f"{row['bom_process_loss_percentage']:.2f}%"
#         row['process_loss_difference'] = f"{row['process_loss_difference']:.2f}%"
#
#         row['planned_qty_for_operation'] = row.get('qty_to_manufacture', 0)
#         row['actual_qty_for_operation'] = row.get('manufactured_qty', 0)
#         row['qty_difference'] = row['planned_qty_for_operation'] - row['actual_qty_for_operation']
#
#         if row['work_order'] != current_work_order:
#             data.append({
#                 "work_order": row['work_order'],
#                 "item_code": row['item_code'],
#                 "product_name": row['product_name'],
#                 "qty_to_manufacture": row['qty_to_manufacture'],
#                 "material_transferred": row['material_transferred'],
#                 "manufactured_qty": row['manufactured_qty'],
#                 "process_loss_qty": row['process_loss_qty'],
#                 "bom_process_loss_percentage": row['bom_process_loss_percentage'],
#                 "process_loss_percentage": row['process_loss_percentage'],
#                 "process_loss_difference": row['process_loss_difference'],
#                 "process_loss_difference_qty": row['process_loss_difference_qty'],
#                 "total_finished_goods": row['total_finished_goods'],
#                 "bom_link": row['bom_link'],
#                 "planned_work_order_total": row['planned_work_order_total'],
#                 "actual_work_order_total": row['actual_work_order_total'],
#                 "work_order_difference": row['work_order_difference'],
#                 "operation": row['operation'],
#                 "workstation": row['workstation'],
#                 "planned_operating_cost": row['planned_operating_cost'],
#                 "actual_operating_cost": row['actual_operating_cost'],
#                 "cost_difference": row['cost_difference'],
#                 "planned_operation_time": row['planned_operation_time'],
#                 "actual_operation_time": row['actual_operation_time'],
#                 "time_difference": row['time_difference'],
#                 "operation_status": row['operation_status'],
#                 "actual_operation_time_per_qty": row['actual_operation_time_per_qty'],
#                 "planned_qty_for_operation": row['planned_qty_for_operation'],
#                 "actual_qty_for_operation": row['actual_qty_for_operation'],
#                 "qty_difference": row['qty_difference'],
#                 "planned_cost_per_operation": row['planned_cost_per_operation'],
#                 "actual_cost_per_operation": row['actual_cost_per_operation'],
#                 "cost_difference_per_operation": row['cost_difference_per_operation']
#             })
#             current_work_order = row['work_order']
#
#     return columns, data
#
#


















#  --------------------------------------------------------------





# ================================================================
# ================================================================











# ================================================================
# ================================================================







# # ===============  Working 004  =====================














#
#
# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
#         {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "planned_qty_for_operation", "label": "Planned Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "actual_qty_for_operation", "label": "Actual Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "qty_difference", "label": "Qty Difference", "fieldtype": "Float", "width": 200},
#         {"fieldname": "planned_cost_per_operation", "label": "Planned Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_cost_per_operation", "label": "Actual Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
#             item.item_name AS product_name,
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#             op.status AS operation_status,
#             (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
#
#             (CASE WHEN op.planned_operating_cost > 0 THEN (op.planned_operating_cost / op.time_in_mins) ELSE 0 END) AS planned_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
#         WHERE wo.docstatus = 1 {conditions}
#         ORDER BY wo.name, op.operation
#     """, filters, as_dict=1)
#
#     data = []
#
#     for row in work_orders:
#         row['process_loss_percentage'] = f"{row['process_loss_percentage']:.2f}%"
#         row['bom_process_loss_percentage'] = f"{row['bom_process_loss_percentage']:.2f}%"
#         row['process_loss_difference'] = f"{row['process_loss_difference']:.2f}%"
#
#         row['planned_qty_for_operation'] = row.get('qty_to_manufacture', 0)
#         row['actual_qty_for_operation'] = row.get('manufactured_qty', 0)
#         row['qty_difference'] = row['planned_qty_for_operation'] - row['actual_qty_for_operation']
#
#         data.append({
#             "work_order": row['work_order'],
#             "item_code": row['item_code'],
#             "product_name": row['product_name'],
#             "qty_to_manufacture": row['qty_to_manufacture'],
#             "material_transferred": row['material_transferred'],
#             "manufactured_qty": row['manufactured_qty'],
#             "process_loss_qty": row['process_loss_qty'],
#             "bom_process_loss_percentage": row['bom_process_loss_percentage'],
#             "process_loss_percentage": row['process_loss_percentage'],
#             "process_loss_difference": row['process_loss_difference'],
#             "process_loss_difference_qty": row['process_loss_difference_qty'],
#             "total_finished_goods": row['total_finished_goods'],
#             "bom_link": row['bom_link'],
#             "planned_work_order_total": row['planned_work_order_total'],
#             "actual_work_order_total": row['actual_work_order_total'],
#             "work_order_difference": row['work_order_difference'],
#             "operation": row['operation'],
#             "workstation": row['workstation'],
#             "planned_operating_cost": row['planned_operating_cost'],
#             "actual_operating_cost": row['actual_operating_cost'],
#             "cost_difference": row['cost_difference'],
#             "planned_operation_time": row['planned_operation_time'],
#             "actual_operation_time": row['actual_operation_time'],
#             "time_difference": row['time_difference'],
#             "operation_status": row['operation_status'],
#             "actual_operation_time_per_qty": row['actual_operation_time_per_qty'],
#             "planned_qty_for_operation": row['planned_qty_for_operation'],
#             "actual_qty_for_operation": row['actual_qty_for_operation'],
#             "qty_difference": row['qty_difference'],
#             "planned_cost_per_operation": row['planned_cost_per_operation'],
#             "actual_cost_per_operation": row['actual_cost_per_operation'],
#             "cost_difference_per_operation": row['cost_difference_per_operation']
#         })
#
#     return columns, data

























# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
#         {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "planned_qty_for_operation", "label": "Planned Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "actual_qty_for_operation", "label": "Actual Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "qty_difference", "label": "Qty Difference", "fieldtype": "Float", "width": 200},
#         {"fieldname": "planned_cost_per_operation", "label": "Planned Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_cost_per_operation", "label": "Actual Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
#             item.item_name AS product_name,
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#             op.status AS operation_status,
#             (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
#             (CASE WHEN wo.produced_qty > 0 THEN (op.planned_operating_cost / op.time_in_mins) ELSE 0 END) AS planned_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
#         WHERE wo.docstatus = 1 {conditions}
#     """, filters, as_dict=True)
#
#     data = []
#     aggregated_work_order = None
#     current_work_order = None
#
#     for row in work_orders:
#         if current_work_order != row['work_order']:
#             if aggregated_work_order:
#                 data.append(aggregated_work_order)
#
#             aggregated_work_order = {
#                 "work_order": row.get('work_order'),
#                 "item_code": row.get('item_code'),
#                 "product_name": row.get('product_name'),
#                 "qty_to_manufacture": row.get('qty_to_manufacture'),
#                 "material_transferred": row.get('material_transferred'),
#                 "manufactured_qty": row.get('manufactured_qty'),
#                 "process_loss_qty": row.get('process_loss_qty'),
#                 "bom_process_loss_percentage": row.get('bom_process_loss_percentage'),
#                 "process_loss_percentage": row.get('process_loss_percentage'),
#                 "process_loss_difference": row.get('process_loss_difference'),
#                 "process_loss_difference_qty": row.get('process_loss_difference_qty'),
#                 "total_finished_goods": row.get('total_finished_goods'),
#                 "bom_link": row.get('bom_link'),
#                 "planned_work_order_total": row.get('planned_work_order_total'),
#                 "actual_work_order_total": row.get('actual_work_order_total'),
#                 "work_order_difference": row.get('work_order_difference'),
#                 "operation": None,
#                 "workstation": None,
#                 "planned_operating_cost": None,
#                 "actual_operating_cost": None,
#                 "cost_difference": None,
#                 "planned_operation_time": None,
#                 "actual_operation_time": None,
#                 "time_difference": None,
#                 "operation_status": None,
#                 "actual_operation_time_per_qty": None,
#                 "planned_qty_for_operation": None,
#                 "actual_qty_for_operation": None,
#                 "qty_difference": None,
#                 "planned_cost_per_operation": None,
#                 "actual_cost_per_operation": None,
#                 "cost_difference_per_operation": None
#             }
#             current_work_order = row.get('work_order')
#
#         data.append({
#             "work_order": None,
#             "item_code": None,
#             "product_name": None,
#             "qty_to_manufacture": None,
#             "material_transferred": None,
#             "manufactured_qty": None,
#             "process_loss_qty": None,
#             "bom_process_loss_percentage": None,
#             "process_loss_percentage": None,
#             "process_loss_difference": None,
#             "process_loss_difference_qty": None,
#             "total_finished_goods": None,
#             "bom_link": None,
#             "planned_work_order_total": None,
#             "actual_work_order_total": None,
#             "work_order_difference": None,
#             "operation": row.get('operation'),
#             "workstation": row.get('workstation'),
#             "planned_operating_cost": row.get('planned_operating_cost'),
#             "actual_operating_cost": row.get('actual_operating_cost'),
#             "cost_difference": row.get('cost_difference'),
#             "planned_operation_time": row.get('planned_operation_time'),
#             "actual_operation_time": row.get('actual_operation_time'),
#             "time_difference": row.get('time_difference'),
#             "operation_status": row.get('operation_status'),
#             "actual_operation_time_per_qty": row.get('actual_operation_time_per_qty'),
#             "planned_qty_for_operation": row.get('planned_qty_for_operation'),
#             "actual_qty_for_operation": row.get('actual_qty_for_operation'),
#             "qty_difference": row.get('qty_difference'),
#             "planned_cost_per_operation": row.get('planned_cost_per_operation'),
#             "actual_cost_per_operation": row.get('actual_cost_per_operation'),
#             "cost_difference_per_operation": row.get('cost_difference_per_operation')
#         })
#
#     if aggregated_work_order:
#         data.append(aggregated_work_order)
#
#     return columns, data













































#
#
#
# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
#         {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "planned_qty_for_operation", "label": "Planned Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "actual_qty_for_operation", "label": "Actual Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "qty_difference", "label": "Qty Difference", "fieldtype": "Float", "width": 200},
#         {"fieldname": "planned_cost_per_operation", "label": "Planned Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_cost_per_operation", "label": "Actual Cost Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
#             item.item_name AS product_name,
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#             op.status AS operation_status,
#             (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
#             (CASE WHEN wo.produced_qty > 0 THEN (op.planned_operating_cost / op.time_in_mins) ELSE 0 END) AS planned_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
#         WHERE wo.docstatus = 1 {conditions}
#     """, filters, as_dict=True)
#
#
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         if current_work_order != row['work_order']:
#             current_work_order = row['work_order']
#             data.append({
#                 "work_order": row.get('work_order'),
#                 "item_code": row.get('item_code'),
#                 "product_name": row.get('product_name'),
#                 "qty_to_manufacture": row.get('qty_to_manufacture'),
#                 "material_transferred": row.get('material_transferred'),
#                 "manufactured_qty": row.get('manufactured_qty'),
#                 "process_loss_qty": row.get('process_loss_qty'),
#                 "bom_process_loss_percentage": row.get('bom_process_loss_percentage'),
#                 "process_loss_percentage": row.get('process_loss_percentage'),
#                 "process_loss_difference": row.get('process_loss_difference'),
#                 "process_loss_difference_qty": row.get('process_loss_difference_qty'),
#                 "total_finished_goods": row.get('total_finished_goods'),
#                 "bom_link": row.get('bom_link'),
#                 "planned_work_order_total": row.get('planned_work_order_total'),
#                 "actual_work_order_total": row.get('actual_work_order_total'),
#                 "work_order_difference": row.get('work_order_difference')
#             })
#
#         data.append({
#             "work_order": None,
#             "item_code": None,
#             "product_name": None,
#             "qty_to_manufacture": None,
#             "material_transferred": None,
#             "manufactured_qty": None,
#             "process_loss_qty": None,
#             "bom_process_loss_percentage": None,
#             "process_loss_percentage": None,
#             "process_loss_difference": None,
#             "process_loss_difference_qty": None,
#             "total_finished_goods": None,
#             "bom_link": None,
#             "planned_work_order_total": None,
#             "actual_work_order_total": None,
#             "work_order_difference": None,
#             "operation": row.get('operation'),
#             "workstation": row.get('workstation'),
#             "planned_operating_cost": row.get('planned_operating_cost'),
#             "actual_operating_cost": row.get('actual_operating_cost'),
#             "cost_difference": row.get('cost_difference'),
#             "planned_operation_time": row.get('planned_operation_time'),
#             "actual_operation_time": row.get('actual_operation_time'),
#             "time_difference": row.get('time_difference'),
#             "operation_status": row.get('operation_status'),
#             "actual_operation_time_per_qty": row.get('actual_operation_time_per_qty'),
#             "planned_qty_for_operation": row.get('planned_qty_for_operation'),
#             "actual_qty_for_operation": row.get('actual_qty_for_operation'),
#             "qty_difference": row.get('qty_difference'),
#             "planned_cost_per_operation": row.get('planned_cost_per_operation'),
#             "actual_cost_per_operation": row.get('actual_cost_per_operation'),
#             "cost_difference_per_operation": row.get('cost_difference_per_operation')
#         })
#
#     return columns, data
#






















#
#
#
#
# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
#         {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "completed_qty", "label": "Completed Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty", "label": "Process Loss Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
#             item.item_name AS product_name,
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#             op.status AS operation_status,
#             (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
#             op.completed_qty AS completed_qty,                -- Completed quantity for operation
#             op.process_loss_qty AS process_loss_qty,          -- Process loss quantity for operation
#             (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
#         WHERE wo.docstatus = 1 {conditions}
#     """, filters, as_dict=True)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         if current_work_order != row['work_order']:
#             current_work_order = row['work_order']
#             data.append({
#                 "work_order": row.get('work_order'),
#                 "item_code": row.get('item_code'),
#                 "product_name": row.get('product_name'),
#                 "qty_to_manufacture": row.get('qty_to_manufacture'),
#                 "material_transferred": row.get('material_transferred'),
#                 "manufactured_qty": row.get('manufactured_qty'),
#                 "process_loss_qty": row.get('process_loss_qty'),
#                 "bom_process_loss_percentage": row.get('bom_process_loss_percentage'),
#                 "process_loss_percentage": row.get('process_loss_percentage'),
#                 "process_loss_difference": row.get('process_loss_difference'),
#                 "process_loss_difference_qty": row.get('process_loss_difference_qty'),
#                 "total_finished_goods": row.get('total_finished_goods'),
#                 "bom_link": row.get('bom_link'),
#                 "planned_work_order_total": row.get('planned_work_order_total'),
#                 "actual_work_order_total": row.get('actual_work_order_total'),
#                 "work_order_difference": row.get('work_order_difference')
#             })
#
#         data.append({
#             "work_order": None,
#             "item_code": None,
#             "product_name": None,
#             "qty_to_manufacture": None,
#             "material_transferred": None,
#             "manufactured_qty": None,
#             "process_loss_qty": None,
#             "bom_process_loss_percentage": None,
#             "process_loss_percentage": None,
#             "process_loss_difference": None,
#             "process_loss_difference_qty": None,
#             "total_finished_goods": None,
#             "bom_link": None,
#             "planned_work_order_total": None,
#             "actual_work_order_total": None,
#             "work_order_difference": None,
#             "operation": row.get('operation'),
#             "workstation": row.get('workstation'),
#             "planned_operating_cost": row.get('planned_operating_cost'),
#             "actual_operating_cost": row.get('actual_operating_cost'),
#             "cost_difference": row.get('cost_difference'),
#             "planned_operation_time": row.get('planned_operation_time'),
#             "actual_operation_time": row.get('actual_operation_time'),
#             "time_difference": row.get('time_difference'),
#             "operation_status": row.get('operation_status'),
#             "actual_operation_time_per_qty": row.get('actual_operation_time_per_qty'),
#             "completed_qty": row.get('completed_qty'),
#             "process_loss_qty": row.get('process_loss_qty'),
#             "cost_difference_per_operation": row.get('cost_difference_per_operation')
#         })
#
#     return columns, data

























# def execute(filters=None):
#     if not filters:
#         filters = {}
#
#     columns = [
#         {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
#         {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
#         {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
#         {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
#         {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
#         {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty_wo", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
#         {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
#         {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
#         {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
#         {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
#         {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
#         {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
#         {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
#         {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
#         {"fieldname": "completed_qty", "label": "Completed Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "process_loss_qty_op", "label": "Process Loss Qty for Operation", "fieldtype": "Float", "width": 200},
#         {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
#             item.item_name AS product_name,
#             wo.qty AS qty_to_manufacture,
#             wo.material_transferred_for_manufacturing AS material_transferred,
#             wo.produced_qty AS manufactured_qty,
#             (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty_wo,
#             (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
#             bom.process_loss_percentage AS bom_process_loss_percentage,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
#              ELSE
#                 0
#              END) AS process_loss_difference,
#             (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
#                 ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
#              ELSE
#                 0
#              END) AS process_loss_difference_qty,
#             (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
#             bom.name AS bom_link,
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
#             op.status AS operation_status,
#             (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
#             op.completed_qty AS completed_qty,                -- Completed quantity for operation
#             op.process_loss_qty AS process_loss_qty_op,          -- Process loss quantity for operation
#             (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
#             (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
#         FROM `tabWork Order` wo
#         JOIN `tabWork Order Operation` op ON wo.name = op.parent
#         LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
#         LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
#         WHERE wo.docstatus = 1 {conditions}
#     """, filters, as_dict=True)
#
#     data = []
#     current_work_order = None
#
#     for row in work_orders:
#         if current_work_order != row['work_order']:
#             current_work_order = row['work_order']
#             data.append({
#                 "work_order": row.get('work_order'),
#                 "item_code": row.get('item_code'),
#                 "product_name": row.get('product_name'),
#                 "qty_to_manufacture": row.get('qty_to_manufacture'),
#                 "material_transferred": row.get('material_transferred'),
#                 "manufactured_qty": row.get('manufactured_qty'),
#                 "process_loss_qty_wo": row.get('process_loss_qty_wo'),
#                 "bom_process_loss_percentage": row.get('bom_process_loss_percentage'),
#                 "process_loss_percentage": row.get('process_loss_percentage'),
#                 "process_loss_difference": row.get('process_loss_difference'),
#                 "process_loss_difference_qty": row.get('process_loss_difference_qty'),
#                 "total_finished_goods": row.get('total_finished_goods'),
#                 "bom_link": row.get('bom_link'),
#                 "planned_work_order_total": row.get('planned_work_order_total'),
#                 "actual_work_order_total": row.get('actual_work_order_total'),
#                 "work_order_difference": row.get('work_order_difference')
#             })
#
#         data.append({
#             "work_order": None,
#             "item_code": None,
#             "product_name": None,
#             "qty_to_manufacture": None,
#             "material_transferred": None,
#             "manufactured_qty": None,
#             "process_loss_qty_wo": None,
#             "bom_process_loss_percentage": None,
#             "process_loss_percentage": None,
#             "process_loss_difference": None,
#             "process_loss_difference_qty": None,
#             "total_finished_goods": None,
#             "bom_link": None,
#             "planned_work_order_total": None,
#             "actual_work_order_total": None,
#             "work_order_difference": None,
#             "operation": row.get('operation'),
#             "workstation": row.get('workstation'),
#             "planned_operating_cost": row.get('planned_operating_cost'),
#             "actual_operating_cost": row.get('actual_operating_cost'),
#             "cost_difference": row.get('cost_difference'),
#             "planned_operation_time": row.get('planned_operation_time'),
#             "actual_operation_time": row.get('actual_operation_time'),
#             "time_difference": row.get('time_difference'),
#             "operation_status": row.get('operation_status'),
#             "actual_operation_time_per_qty": row.get('actual_operation_time_per_qty'),
#             "completed_qty": row.get('completed_qty'),
#             "process_loss_qty_op": row.get('process_loss_qty_op'),
#             "cost_difference_per_operation": row.get('cost_difference_per_operation')
#         })
#
#     return columns, data













def execute(filters=None):
    if not filters:
        filters = {}

    columns = [
        {"fieldname": "work_order", "label": "Work Order", "fieldtype": "Link", "options": "Work Order", "width": 200},
        {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 150},
        {"fieldname": "product_name", "label": "Product Name", "fieldtype": "Data", "width": 200},
        {"fieldname": "qty_to_manufacture", "label": "Qty To Manufacture", "fieldtype": "Float", "width": 200},
        {"fieldname": "material_transferred", "label": "Material Transferred for Manufacturing", "fieldtype": "Float", "width": 300},
        {"fieldname": "manufactured_qty", "label": "Manufactured Qty", "fieldtype": "Float", "width": 200},
        # {"fieldname": "process_loss_qty_wo", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
        {"fieldname": "process_loss_qty_wo", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200},
        # {"fieldname": "process_loss_qty_wo", "label": "Process Loss Qty", "fieldtype": "Float", "width": 200,"color": "#8B0000"},

        {"fieldname": "bom_process_loss_percentage", "label": "BOM Process Loss (%)", "fieldtype": "Data", "width": 250},
        {"fieldname": "process_loss_percentage", "label": "Process Loss Percentage (%)", "fieldtype": "Data", "width": 250},
        {"fieldname": "process_loss_difference", "label": "Process Loss Difference (%)", "fieldtype": "Data", "width": 250},
        {"fieldname": "process_loss_difference_qty", "label": "Process Loss Difference Qty", "fieldtype": "Float", "width": 250},
        {"fieldname": "total_finished_goods", "label": "Total Finished Goods", "fieldtype": "Float", "width": 200},
        {"fieldname": "bom_link", "label": "BOM Link", "fieldtype": "Link", "options": "BOM", "width": 200},
        {"fieldname": "planned_work_order_total", "label": "Planned Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
        {"fieldname": "actual_work_order_total", "label": "Actual Work Order Total (£ or ج.م)", "fieldtype": "Currency", "width": 300},
        {"fieldname": "work_order_difference", "label": "Work Order Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
        {"fieldname": "operation", "label": "Operation", "fieldtype": "Data", "width": 200},
        {"fieldname": "workstation", "label": "Workstation", "fieldtype": "Data", "width": 200},
        {"fieldname": "planned_operating_cost", "label": "Planned Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
        {"fieldname": "actual_operating_cost", "label": "Actual Operating Cost (£ or ج.م)", "fieldtype": "Currency", "width": 300},
        {"fieldname": "cost_difference", "label": "Cost Difference (£ or ج.م)", "fieldtype": "Currency", "width": 300},
        {"fieldname": "planned_operation_time", "label": "Planned Operation Time (mins)", "fieldtype": "Float", "width": 300},
        {"fieldname": "actual_operation_time", "label": "Actual Operation Time (mins)", "fieldtype": "Float", "width": 300},
        {"fieldname": "time_difference", "label": "Time Difference (mins)", "fieldtype": "Float", "width": 200},
        {"fieldname": "operation_status", "label": "Operation Status", "fieldtype": "Data", "width": 200},
        {"fieldname": "actual_operation_time_per_qty", "label": "Actual Operation Time Per Qty (mins)", "fieldtype": "Float", "width": 300},
        {"fieldname": "completed_qty", "label": "Completed Qty for Operation", "fieldtype": "Float", "width": 250},
        {"fieldname": "process_loss_qty_op", "label": "Process Loss Qty for Operation", "fieldtype": "Float", "width": 250},
        {"fieldname": "cost_difference_per_operation", "label": "Cost Difference Per Operation (£ or ج.م)", "fieldtype": "Currency", "width": 300}
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
            item.item_name AS product_name,
            wo.qty AS qty_to_manufacture,
            wo.material_transferred_for_manufacturing AS material_transferred,
            wo.produced_qty AS manufactured_qty,
            (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty_wo,
            (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
            bom.process_loss_percentage AS bom_process_loss_percentage,
            (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
                ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
             ELSE
                0
             END) AS process_loss_difference,
            (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
                ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
             ELSE
                0
             END) AS process_loss_difference_qty,
            (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
            bom.name AS bom_link,
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
            op.status AS operation_status,
            (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
            op.completed_qty AS completed_qty,                -- Completed quantity for operation
            op.process_loss_qty AS process_loss_qty_op,          -- Process loss quantity for operation
            (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
            (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
        FROM `tabWork Order` wo
        JOIN `tabWork Order Operation` op ON wo.name = op.parent
        LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
        LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
        WHERE wo.docstatus = 1 {conditions}
    """, filters, as_dict=True)

    data = []
    current_work_order = None

    for row in work_orders:
        row['process_loss_percentage'] = f"{row['process_loss_percentage']:.2f}%"
        row['bom_process_loss_percentage'] = f"{row['bom_process_loss_percentage']:.2f}%"
        row['process_loss_difference'] = f"{row['process_loss_difference']:.2f}%"

        row['planned_qty_for_operation'] = row.get('qty_to_manufacture', 0)
        row['actual_qty_for_operation'] = row.get('manufactured_qty', 0)
        row['qty_difference'] = row['planned_qty_for_operation'] - row['actual_qty_for_operation']

    for row in work_orders:
        if current_work_order != row['work_order']:
            current_work_order = row['work_order']

            data.append({
                "work_order": row.get('work_order'),
                "item_code": row.get('item_code'),
                "product_name": row.get('product_name'),
                "qty_to_manufacture": row.get('qty_to_manufacture'),
                "material_transferred": row.get('material_transferred'),
                "manufactured_qty": row.get('manufactured_qty'),
                "process_loss_qty_wo": row.get('process_loss_qty_wo'),
                "bom_process_loss_percentage": row.get('bom_process_loss_percentage'),
                "process_loss_percentage": row.get('process_loss_percentage'),
                "process_loss_difference": row.get('process_loss_difference'),
                "process_loss_difference_qty": row.get('process_loss_difference_qty'),
                "total_finished_goods": row.get('total_finished_goods'),
                "bom_link": row.get('bom_link'),
                "planned_work_order_total": row.get('planned_work_order_total'),
                "actual_work_order_total": row.get('actual_work_order_total'),
                "work_order_difference": row.get('work_order_difference')
            })

        data.append({
            "work_order": None,
            "item_code": None,
            "product_name": None,
            "qty_to_manufacture": None,
            "material_transferred": None,
            "manufactured_qty": None,
            "process_loss_qty_wo": None,
            "bom_process_loss_percentage": None,
            "process_loss_percentage": None,
            "process_loss_difference": None,
            "process_loss_difference_qty": None,
            "total_finished_goods": None,
            "bom_link": None,
            "planned_work_order_total": None,
            "actual_work_order_total": None,
            "work_order_difference": None,
            "operation": row.get('operation'),
            "workstation": row.get('workstation'),
            "planned_operating_cost": row.get('planned_operating_cost'),
            "actual_operating_cost": row.get('actual_operating_cost'),
            "cost_difference": row.get('cost_difference'),
            "planned_operation_time": row.get('planned_operation_time'),
            "actual_operation_time": row.get('actual_operation_time'),
            "time_difference": row.get('time_difference'),
            "operation_status": row.get('operation_status'),
            "actual_operation_time_per_qty": row.get('actual_operation_time_per_qty'),
            "completed_qty": row.get('completed_qty'),
            "process_loss_qty_op": row.get('process_loss_qty_op'),
            "cost_difference_per_operation": row.get('cost_difference_per_operation')
        })

    return columns, data















#  --------------------------------------------------------------





# ================================================================
# ================================================================





@frappe.whitelist()
def test_method():
    frappe.msgprint("test  --- ")
    return "Method called successfully!"








@frappe.whitelist()
def get_work_order_data(filters):
    if isinstance(filters, str):
        filters = json.loads(filters)

    conditions = ""
    if filters.get("work_order"):
        conditions += "AND wo.name = %(work_order)s "
    if filters.get("item_code"):
        conditions += "AND wo.production_item = %(item_code)s "

    work_orders = frappe.db.sql(f"""
        SELECT
            wo.name AS work_order,
            (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty_wo,
            (wo.material_transferred_for_manufacturing - wo.produced_qty) - 
            ((bom.process_loss_percentage / 100) * wo.qty) AS process_loss_difference_qty
        FROM `tabWork Order` wo
        LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
        WHERE wo.docstatus = 1 {conditions}
    """, filters, as_dict=True)

    return work_orders





















# ================================================================
# ================================================================

































