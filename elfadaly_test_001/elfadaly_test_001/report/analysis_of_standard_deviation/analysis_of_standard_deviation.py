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





def execute(filters=None):
    if not filters:
        filters = {}

    def get_columns():
        lang = frappe.local.lang or 'en'

        if lang == 'ar':
            labels = {
                "work_order": "أمر الشغل",
                "item_code": "كود المنتج",
                "product_name": "اسم المنتج",
                "qty_to_manufacture": "كمية للتصنيع المحددة فى أمر الشغل",
                "material_transferred": "كمية المواد المنقولة للتصنيع - المواد الخام",
                "manufactured_qty": "الكمية المصنعة الفعلية",
                "process_loss_qty_wo": "كمية الفاقد من أمر الشغل",
                "bom_process_loss_percentage": "نسبة فاقد BOM (%) القياسي",
                "process_loss_percentage": "نسبة الفاقد (%) من أمر الشغل",
                "process_loss_difference": "فرق الفاقد (%) من أمر الشغل - الفعلي",
                "process_loss_difference_qty": "فرق كمية الفاقد - الفعلي",
                # "total_finished_goods": "إجمالي البضائع الجاهزة",
                "bom_link": "الريسبي",
                "planned_work_order_total": "إجمالي تكلفة أمر الشغل المخطط (£ أو ج.م)",
                "actual_work_order_total": "إجمالي تكلفة أمر الشغل الفعلي (£ أو ج.م)",
                "work_order_difference": "فرق تكلفة أمر الشغل (£ أو ج.م)",
                "operation": "عمليات الإنتاج",
                "workstation": "محطات أمر الشغل",
                "planned_operating_cost": "تكلفة التشغيل المخططة - القياسية (£ أو ج.م)",
                "actual_operating_cost": "تكلفة التشغيل الفعلية (£ أو ج.م)",
                "cost_difference": "فرق التكلفة (£ أو ج.م)",
                "planned_operation_time": "الوقت المخطط للعمل (دقائق)",
                "actual_operation_time": "الوقت الفعلي للعمل (دقائق)",
                "time_difference": "فرق الوقت (دقائق)",
                "planned_operation_time_hours": "الوقت المخطط للعمل (ساعات)",
                "actual_operation_time_hours": "الوقت الفعلي للعمل (ساعات)",
                "time_difference_hours": "فرق الوقت (ساعات)",
                "operation_status": "حالة العملية",
                "actual_operation_time_per_qty": "الوقت الفعلي للعمل لكل كمية (دقائق)",
                "completed_qty": "الكمية المكتملة للعملية",
                "process_loss_qty_op": "كمية الفاقد للعملية",
                "cost_difference_per_operation": "فرق التكلفة لكل عملية (£ أو ج.م)"
            }
        else:
            labels = {
                "work_order": "Work Order",
                "item_code": "Item Code",
                "product_name": "Product Name",
                "qty_to_manufacture": "Qty To Manufacture",
                "material_transferred": "Material Transferred for Manufacturing",
                "manufactured_qty": "Manufactured Qty",
                "process_loss_qty_wo": "Process Loss Qty",
                "bom_process_loss_percentage": "BOM Process Loss (%)",
                "process_loss_percentage": "Process Loss Percentage (%)",
                "process_loss_difference": "Process Loss Difference (%)",
                "process_loss_difference_qty": "Process Loss Difference Qty",
                # "total_finished_goods": "Total Finished Goods",
                "bom_link": "Recipe",
                "planned_work_order_total": "Planned Work Order Total (£ or ج.م)",
                "actual_work_order_total": "Actual Work Order Total (£ or ج.م)",
                "work_order_difference": "Work Order Difference (£ or ج.م)",
                "operation": "Operation",
                "workstation": "Workstation",
                "planned_operating_cost": "Planned Operating Cost (£ or ج.م)",
                "actual_operating_cost": "Actual Operating Cost (£ or ج.م)",
                "cost_difference": "Cost Difference (£ or ج.م)",
                "planned_operation_time": "Planned Operation Time (mins)",
                "actual_operation_time": "Actual Operation Time (mins)",
                "time_difference": "Time Difference (mins)",
                "planned_operation_time_hours": "Planned Operation Time (hrs)",
                "actual_operation_time_hours": "Actual Operation Time (hrs)",
                "time_difference_hours": "Time Difference (hrs)",
                "operation_status": "Operation Status",
                "actual_operation_time_per_qty": "Actual Operation Time Per Qty (mins)",
                "completed_qty": "Completed Qty for Operation",
                "process_loss_qty_op": "Process Loss Qty for Operation",
                "cost_difference_per_operation": "Cost Difference Per Operation (£ or ج.م)"
            }

        columns = [
            {"fieldname": "work_order", "label": labels["work_order"], "fieldtype": "Link", "options": "Work Order",
             "width": 200},
            {"fieldname": "item_code", "label": labels["item_code"], "fieldtype": "Link", "options": "Item",
             "width": 150},
            {"fieldname": "product_name", "label": labels["product_name"], "fieldtype": "Data", "width": 200},
            {"fieldname": "qty_to_manufacture", "label": labels["qty_to_manufacture"], "fieldtype": "Float",
             "width": 300},
            {"fieldname": "material_transferred", "label": labels["material_transferred"], "fieldtype": "Float",
             "width": 300},
            {"fieldname": "manufactured_qty", "label": labels["manufactured_qty"], "fieldtype": "Float", "width": 300},
            {"fieldname": "process_loss_qty_wo", "label": labels["process_loss_qty_wo"], "fieldtype": "Float",
             "width": 300},
            # {"fieldname": "bom_process_loss_percentage", "label": labels["bom_process_loss_percentage"],
            #  "fieldtype": "Float", "width": 300},
            {"fieldname": "bom_process_loss_percentage", "label": labels["bom_process_loss_percentage"],
             "fieldtype": "Data", "width": 300},
            # {"fieldname": "process_loss_percentage", "label": labels["process_loss_percentage"], "fieldtype": "Float",
            #  "width": 300},
            {"fieldname": "process_loss_percentage", "label": labels["process_loss_percentage"], "fieldtype": "Data",
             "width": 300},
            # {"fieldname": "process_loss_difference", "label": labels["process_loss_difference"], "fieldtype": "Float",
            #  "width": 300},
            {"fieldname": "process_loss_difference", "label": labels["process_loss_difference"], "fieldtype": "Data",
             "width": 300},
            {"fieldname": "process_loss_difference_qty", "label": labels["process_loss_difference_qty"],
             "fieldtype": "Float", "width": 300},
            # {"fieldname": "total_finished_goods", "label": labels["total_finished_goods"], "fieldtype": "Float", "width": 300},
            {"fieldname": "bom_link", "label": labels["bom_link"], "fieldtype": "Link", "options": "BOM", "width": 200},
            {"fieldname": "planned_work_order_total", "label": labels["planned_work_order_total"],
             "fieldtype": "Currency", "width": 300},
            {"fieldname": "actual_work_order_total", "label": labels["actual_work_order_total"],
             "fieldtype": "Currency", "width": 300},
            {"fieldname": "work_order_difference", "label": labels["work_order_difference"], "fieldtype": "Currency",
             "width": 300},
            {"fieldname": "operation", "label": labels["operation"], "fieldtype": "Data", "width": 200},
            {"fieldname": "workstation", "label": labels["workstation"], "fieldtype": "Data", "width": 200},
            {"fieldname": "planned_operating_cost", "label": labels["planned_operating_cost"], "fieldtype": "Currency",
             "width": 300},
            {"fieldname": "actual_operating_cost", "label": labels["actual_operating_cost"], "fieldtype": "Currency",
             "width": 300},
            {"fieldname": "cost_difference", "label": labels["cost_difference"], "fieldtype": "Currency", "width": 300},
            {"fieldname": "planned_operation_time", "label": labels["planned_operation_time"], "fieldtype": "Float",
             "width": 250},
            {"fieldname": "actual_operation_time", "label": labels["actual_operation_time"], "fieldtype": "Float",
             "width": 200},
            {"fieldname": "time_difference", "label": labels["time_difference"], "fieldtype": "Float", "width": 200},
            # {"fieldname": "planned_operation_time_hours", "label": labels["planned_operation_time_hours"],
            #  "fieldtype": "Float", "width": 250},
            {"fieldname": "planned_operation_time_hours", "label": labels["planned_operation_time_hours"],
             "fieldtype": "Data", "width": 250},
            # {"fieldname": "actual_operation_time_hours", "label": labels["actual_operation_time_hours"],
            #  "fieldtype": "Float", "width": 250},
            {"fieldname": "actual_operation_time_hours", "label": labels["actual_operation_time_hours"],
             "fieldtype": "Data", "width": 250},
            # {"fieldname": "time_difference_hours", "label": labels["time_difference_hours"], "fieldtype": "Float",
            #  "width": 200},
            {"fieldname": "time_difference_hours", "label": labels["time_difference_hours"], "fieldtype": "Data",
             "width": 200},
            {"fieldname": "operation_status", "label": labels["operation_status"], "fieldtype": "Data", "width": 200},
            {"fieldname": "actual_operation_time_per_qty", "label": labels["actual_operation_time_per_qty"],
             "fieldtype": "Float", "width": 300},
            {"fieldname": "completed_qty", "label": labels["completed_qty"], "fieldtype": "Float", "width": 200},
            {"fieldname": "process_loss_qty_op", "label": labels["process_loss_qty_op"], "fieldtype": "Float",
             "width": 200},
            # {"fieldname": "cost_difference_per_operation", "label": labels["cost_difference_per_operation"],
            #  "fieldtype": "Currency", "width": 250},
        ]

        return columns

    columns = get_columns()


    conditions = ""
    if filters.get("work_order"):
        conditions += "AND wo.name = %(work_order)s "
    if filters.get("item_code"):
        conditions += "AND wo.production_item = %(item_code)s "

    if filters.get("date_from") and filters.get("date_to"):
        conditions += f" AND wo.creation BETWEEN '{filters.get('date_from')}' AND '{filters.get('date_to')}'"
        # conditions.append(f"wo.creation BETWEEN '{filters.get('date_from')}' AND '{filters.get('date_to')}'")

    # work_orders = frappe.db.sql(f"""
    #     SELECT
    #         wo.name AS work_order,
    #         wo.production_item AS item_code,
    #         item.item_name AS product_name,
    #         wo.qty AS qty_to_manufacture,
    #         wo.material_transferred_for_manufacturing AS material_transferred,
    #         wo.produced_qty AS manufactured_qty,
    #         (wo.material_transferred_for_manufacturing - wo.produced_qty) AS process_loss_qty_wo,
    #         (CASE WHEN wo.qty > 0 THEN (wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100 ELSE 0 END) AS process_loss_percentage,
    #         bom.process_loss_percentage AS bom_process_loss_percentage,
    #         (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
    #             ((wo.material_transferred_for_manufacturing - wo.produced_qty) / wo.qty * 100) - bom.process_loss_percentage
    #          ELSE
    #             0
    #          END) AS process_loss_difference,
    #         (CASE WHEN bom.process_loss_percentage IS NOT NULL THEN
    #             ((wo.material_transferred_for_manufacturing - wo.produced_qty) - (bom.process_loss_percentage / 100 * wo.qty))
    #          ELSE
    #             0
    #          END) AS process_loss_difference_qty,
    #         (SELECT COALESCE(SUM(sed.qty), 0) FROM `tabStock Entry Detail` sed WHERE sed.parent = wo.name AND sed.item_code = wo.production_item) AS total_finished_goods,
    #         bom.name AS bom_link,
    #         wo.total_operating_cost AS actual_work_order_total,
    #         wo.planned_operating_cost AS planned_work_order_total,
    #         (wo.total_operating_cost - wo.planned_operating_cost) AS work_order_difference,
    #         op.operation AS operation,
    #         op.workstation AS workstation,
    #         op.planned_operating_cost AS planned_operating_cost,
    #         op.actual_operating_cost AS actual_operating_cost,
    #         (op.actual_operating_cost - op.planned_operating_cost) AS cost_difference,
    #         op.time_in_mins AS planned_operation_time,
    #         op.actual_operation_time AS actual_operation_time,
    #         (op.actual_operation_time - op.time_in_mins) AS time_difference,
    #         (op.time_in_mins / 60) AS planned_operation_time_hours,
    #         (op.actual_operation_time / 60) AS actual_operation_time_hours,
    #         ((op.actual_operation_time - op.time_in_mins) / 60) AS time_difference_hours,
    #         op.status AS operation_status,
    #         (CASE WHEN wo.produced_qty > 0 THEN op.actual_operation_time / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
    #         op.completed_qty AS completed_qty,
    #         op.process_loss_qty AS process_loss_qty_op,
    #         (CASE WHEN op.actual_operation_time > 0 THEN (op.actual_operating_cost / op.actual_operation_time) ELSE 0 END) AS actual_cost_per_operation,
    #         (CASE WHEN op.actual_operation_time > 0 AND op.time_in_mins > 0 THEN ((op.actual_operating_cost / op.actual_operation_time) - (op.planned_operating_cost / op.time_in_mins)) ELSE 0 END) AS cost_difference_per_operation
    #     FROM `tabWork Order` wo
    #     JOIN `tabWork Order Operation` op ON wo.name = op.parent
    #     LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
    #     LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
    #     WHERE wo.docstatus = 1 {conditions}
    #     ORDER BY wo.name, op.idx
    # """, filters, as_dict=True)

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
            COALESCE(op.planned_operating_cost, 0) AS planned_operating_cost,
            COALESCE(op.actual_operating_cost, 0) AS actual_operating_cost,
            (COALESCE(op.actual_operating_cost, 0) - COALESCE(op.planned_operating_cost, 0)) AS cost_difference,
            COALESCE(op.time_in_mins, 0) AS planned_operation_time,
            COALESCE(op.actual_operation_time, 0) AS actual_operation_time,
            (COALESCE(op.actual_operation_time, 0) - COALESCE(op.time_in_mins, 0)) AS time_difference,
            (COALESCE(op.time_in_mins, 0) / 60) AS planned_operation_time_hours,
            (COALESCE(op.actual_operation_time, 0) / 60) AS actual_operation_time_hours,
            ((COALESCE(op.actual_operation_time, 0) - COALESCE(op.time_in_mins, 0)) / 60) AS time_difference_hours,
            op.status AS operation_status,
            (CASE WHEN wo.produced_qty > 0 THEN COALESCE(op.actual_operation_time, 0) / wo.produced_qty ELSE 0 END) AS actual_operation_time_per_qty,
            op.completed_qty AS completed_qty,
            op.process_loss_qty AS process_loss_qty_op,
            (CASE WHEN COALESCE(op.actual_operation_time, 0) > 0 THEN (COALESCE(op.actual_operating_cost, 0) / COALESCE(op.actual_operation_time, 0)) ELSE 0 END) AS actual_cost_per_operation,
            (CASE WHEN COALESCE(op.actual_operation_time, 0) > 0 AND COALESCE(op.time_in_mins, 0) > 0 THEN 
                ((COALESCE(op.actual_operating_cost, 0) / COALESCE(op.actual_operation_time, 0)) - (COALESCE(op.planned_operating_cost, 0) / COALESCE(op.time_in_mins, 0))) 
             ELSE 0 END) AS cost_difference_per_operation
        FROM `tabWork Order` wo
        LEFT JOIN `tabWork Order Operation` op ON wo.name = op.parent
        LEFT JOIN `tabBOM` bom ON bom.name = wo.bom_no
        LEFT JOIN `tabItem` item ON item.item_code = wo.production_item
        WHERE wo.docstatus = 1 {conditions}
        ORDER BY wo.name, op.idx
    """, filters, as_dict=True)

    data = []
    current_work_order = None

    for row in work_orders:

        row['process_loss_percentage'] = f"{row['process_loss_percentage']:.2f}%"
        row['bom_process_loss_percentage'] = f"{row['bom_process_loss_percentage']:.2f}%"
        row['process_loss_difference'] = f"{row['process_loss_difference']:.2f}%"

        row['planned_operation_time_hours'] = f"{row['planned_operation_time_hours']:.2f}    ساعة   "
        row['actual_operation_time_hours'] = f"{row['actual_operation_time_hours']:.2f}    ساعة   "
        row['time_difference_hours'] = f"{row['time_difference_hours']:.2f}    ساعة   "

        # row['planned_qty_for_operation'] = row.get('qty_to_manufacture', 0)
        # row['actual_qty_for_operation'] = row.get('manufactured_qty', 0)
        # row['qty_difference'] = row['planned_qty_for_operation'] - row['actual_qty_for_operation']


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
                    "work_order_difference": row.get('work_order_difference'),
                    "operation": None,
                    "workstation": None,
                    "planned_operating_cost": None,
                    "actual_operating_cost": None,
                    "cost_difference": None,
                    "planned_operation_time": None,
                    "actual_operation_time": None,
                    "time_difference": None,
                    "planned_operation_time_hours": None,
                    "actual_operation_time_hours": None,
                    "time_difference_hours": None,
                    "operation_status": None,
                    "actual_operation_time_per_qty": None,
                    "completed_qty": None,
                    "process_loss_qty_op": None,
                    "cost_difference_per_operation": None,
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
            "planned_operation_time_hours": row.get('planned_operation_time_hours'),

            "actual_operation_time_hours": row.get('actual_operation_time_hours'),
            "time_difference_hours": row.get('time_difference_hours'),
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










