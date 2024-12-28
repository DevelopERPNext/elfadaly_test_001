# Copyright (c) 2024, Mahmoud Khattab
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

import json
from frappe.utils import flt


# from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry




@frappe.whitelist()
def create_print_msg(doc, method=None):
    frappe.msgprint(str("Material Transfer has been created."), alert=True)
    doc.reload()

def validate_branch(doc, method=None):
    # Ensure "Receiving Branch" is set for material transfers
    if doc.stock_entry_type == "Material Transfer" and not doc.get("receiving_branch"):
        frappe.throw("Please specify the Receiving Branch for material transfers.")

def on_update_branch(doc, method=None):
    # If document is saved and is a Material Transfer, send notification to receiving branch
    if doc.docstatus == 0 and doc.stock_entry_type == "Material Transfer":
        frappe.msgprint(str("send notification to receiving branch"), alert=True)
        # doc.send_notification_to_receiving_branch()

# def send_notification_to_receiving_branch_branch(doc, method=None):
#     # Fetch all users associated with the receiving branch
#     if doc.receiving_branch:
#         users = frappe.get_all(
#             "User",
#             filters={"branch": doc.branch_receiving_branch_a_001, "enabled": 1},
#             fields=["name"]
#         )
#         # Send notification email to each user in the receiving branch
#         for user in users:
#             frappe.sendmail(
#                 recipients=user.name,
#                 subject="New Material Transfer awaiting your action",
#                 message=f"A new material transfer has been created for your branch ({doc.branch_receiving_branch_a_001}). Please review and submit."
#             )

def before_submit_branch(doc, method=None):
    # Allow only the receiving branch to submit the document
    user_branch = frappe.db.get_value("User", frappe.session.user, "branch_user_a_001")

    # frappe.msgprint(str(user_branch))

    if doc.stock_entry_type == "Material Transfer" and user_branch != doc.branch_receiving_branch_a_001:
        frappe.throw("Only the receiving branch can submit this transfer document.")








#  Function to perform the calculation based on process_loss_percentage from the BOM associated with the Work Order (bom_no)

@frappe.whitelist()
def calculate_qty(work_order_name, actual_qty, bom_no):
    # Check if actual_qty is a valid number; if not, set it to 0
    try:
        actual_qty = float(actual_qty)
    except ValueError:
        actual_qty = 0

    # Fetch the process loss percentage from the BOM
    bom = frappe.get_doc("BOM", bom_no)
    process_loss_percentage = bom.process_loss_percentage or 0

    # Calculate the adjusted quantity based on process loss
    adjusted_qty = actual_qty * (1 + (process_loss_percentage / 100))

    # Update the qty in Work Order
    work_order = frappe.get_doc("Work Order", work_order_name)
    work_order.qty = adjusted_qty
    # work_order.save()

    return adjusted_qty







@frappe.whitelist()
def get_user_roles_a():
    user = frappe.session.user
    roles = frappe.get_roles(user)
    return roles





# ========================================================
# ========================================================
# =========  START Fetch Qty From Table Scrap Item in BOM  ==============




@frappe.whitelist()
def fetch_bom_check_a_001(doc, method=None):

    stock_entry = frappe.get_doc("Stock Entry", doc) if isinstance(doc, str) else doc

    if stock_entry.docstatus == 0 and stock_entry.stock_entry_type == 'Manufacture':
        bom_check_detail = frappe.get_all(
            "Stock Entry",
            filters={"name": stock_entry.name},
            fields=["bom_check_a_001", ],
        )

        bom_check_info = bom_check_detail[0].get('bom_check_a_001')

        # frappe.msgprint(str(bom_check_info))
        frappe.db.set_value("Stock Entry", stock_entry.name, "bom_check_a_001", 1)



@frappe.whitelist()
def fetch_qty_from_table_scrap_item_in_bom(doc, method=None):

    # if not doc:
    #     frappe.throw(_("Document is required"))

    stock_entry = frappe.get_doc("Stock Entry", doc) if isinstance(doc, str) else doc

    # if stock_entry.docstatus == 0 and stock_entry.stock_entry_type == 'Manufacture':

    # bom_check_a_001

    bom_check_detail = frappe.get_all(
        "Stock Entry",
        filters={"name": stock_entry.name},
        fields=["bom_check_a_001", ],
    )

    bom_check_info = bom_check_detail[0].get('bom_check_a_001')

    # if bom_check_info == 1 or bom_check_info == 0:

    # frappe.db.set_value("Stock Entry", stock_entry.name, "bom_check_a_001", 0)

    # frappe.msgprint(str(bom_check_info))

    # if bom_check_detail:
    #     bom_check_info = bom_check_detail[0].get('bom_check_a_001')

    if bom_check_info == 1:
        stock_entry_items = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": stock_entry.name},
            fields=[
                "name", "item_code", "qty", "uom", "is_finished_item", "is_scrap_item",
                "basic_rate", "bom_no", "item_name", "t_warehouse"
            ]
        )

        bom_no = stock_entry.bom_no
        if not bom_no:
            frappe.throw(_("BOM is not linked with this Stock Entry"))

        bom_fetch_total_cost = frappe.get_all(
            "BOM",
            filters={"name": bom_no},
            fields=["total_cost"]
        )

        # if not bom_fetch_total_cost:
        #     frappe.throw(_("BOM Total Cost not found."))
        #
        # bom_total_cost = bom_fetch_total_cost[0].get('total_cost')

        bom_fetch_bom_scrap_item = frappe.get_all(
            "BOM Scrap Item",
            filters={"parent": bom_no},
            fields=["item_code", "item_name", "stock_qty", "stock_uom", ]
        )

        bom_fetch_bom_scrap_item_qty = None

        # bom_fetch_bom_scrap_item_qty = [item["stock_qty"] for item in bom_fetch_bom_scrap_item if
        #                                 "stock_qty" in item]

        for stock_entry_item in stock_entry_items:
            for bom_scrap_item in bom_fetch_bom_scrap_item:
                if stock_entry_item["item_code"] == bom_scrap_item["item_code"]:
                    bom_fetch_bom_scrap_item_qty = bom_scrap_item.get("stock_qty", 0)

        # if bom_fetch_bom_scrap_item:
        #     bom_fetch_bom_scrap_item_qty = bom_fetch_bom_scrap_item[0].get("stock_qty")
        # else:
        #     bom_fetch_bom_scrap_item_qty = None

        for item_a in stock_entry_items:
            if item_a.get("is_scrap_item") == 1:
                item_code_is_scrap_item = item_a["item_code"]


        work_order = stock_entry.work_order
        if not work_order:
            frappe.throw(_("work_order is not linked with this Stock Entry"))

        work_order_fetch_info = frappe.get_all(
            "Work Order",
            filters={"name": work_order},
            fields=["actual_qty_to_manufacture_a_001"]
        )

        for work_order_item in work_order_fetch_info:
            work_order_fetch_actual_qty_to_manufacture_a_001 = work_order_item.get("actual_qty_to_manufacture_a_001", 0)


        # frappe.msgprint(str(item_code_is_scrap_item))
        # frappe.msgprint(str(bom_no))
        # frappe.msgprint(str(bom_fetch_total_cost))
        # frappe.msgprint(str(bom_fetch_bom_scrap_item))
        #
        # frappe.msgprint(str(bom_fetch_bom_scrap_item_qty), alert=True)
        # frappe.msgprint(str(work_order_fetch_actual_qty_to_manufacture_a_001), alert=True)


        # if isinstance(bom_fetch_bom_scrap_item_qty, (int, float)) and isinstance(
        #         work_order_fetch_actual_qty_to_manufacture_a_001, (int, float)):
        #     result_qty_scrap_item = bom_fetch_bom_scrap_item_qty * work_order_fetch_actual_qty_to_manufacture_a_001
        #     frappe.msgprint(str(result_qty_scrap_item))
        # else:
        #     frappe.throw(_("Ensure both quantities are numeric for calculation."))

        try:
            bom_fetch_bom_scrap_item_qty = float(bom_fetch_bom_scrap_item_qty)
            work_order_fetch_actual_qty_to_manufacture_a_001 = float(work_order_fetch_actual_qty_to_manufacture_a_001)

            result_qty_scrap_item = bom_fetch_bom_scrap_item_qty * work_order_fetch_actual_qty_to_manufacture_a_001
            # frappe.msgprint(_("Resulting Scrap Item Quantity: {0}").format(result_qty_scrap_item))

        except (TypeError, ValueError):
            frappe.throw(_("Ensure both quantities are numeric for calculation."))




        # if bom_fetch_bom_scrap_item_qty is None or work_order_fetch_actual_qty_to_manufacture_a_001 is None:
        #     frappe.throw(_("One or both of the required quantities are missing."))
        #
        # try:
        #     bom_fetch_bom_scrap_item_qty = float(bom_fetch_bom_scrap_item_qty)
        #     work_order_fetch_actual_qty_to_manufacture_a_001 = float(work_order_fetch_actual_qty_to_manufacture_a_001)
        #
        #     result_qty_scrap_item = bom_fetch_bom_scrap_item_qty * work_order_fetch_actual_qty_to_manufacture_a_001
        #     frappe.msgprint(_("Resulting Scrap Item Quantity: {0}").format(result_qty_scrap_item))
        #
        # except ValueError:
        #     frappe.throw(_("Ensure both quantities are numeric for calculation."))






        for item_aa in stock_entry_items:
            if item_aa.get("is_scrap_item") == 1:
                item_code_is_scrap_item_aa = item_aa["item_code"]
                item_qty_is_scrap_item_aa = item_aa["qty"]

                # frappe.msgprint(str(item_code_is_scrap_item_aa), alert=True)
                # frappe.msgprint(str(item_qty_is_scrap_item_aa), alert=True)




                # if isinstance(result_qty_scrap_item, (int, float)) and isinstance(item_qty_is_scrap_item_aa,
                #                                                                   (int, float)):
                #
                #
                #     if item_qty_is_scrap_item_aa > result_qty_scrap_item:
                #         frappe.throw(_("Resulting quantity exceeds the scrap item quantity."))
                #         # frappe.db.set_value("Stock Entry Detail",
                #         #                     {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa},
                #         #                     "qty", result_qty_scrap_item)
                #
                #     elif item_qty_is_scrap_item_aa == result_qty_scrap_item:
                #         frappe.db.set_value("Stock Entry Detail",
                #                             {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa},
                #                             "qty", result_qty_scrap_item)
                #
                #     elif item_qty_is_scrap_item_aa < result_qty_scrap_item:
                #         # frappe.db.set_value("Stock Entry Detail",
                #         #                     {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa},
                #         #                     "qty", item_qty_is_scrap_item_aa)
                #
                #         # frappe.db.sql("""
                #         #                 UPDATE `tabStock Entry Detail`
                #         #                 SET qty = %s
                #         #                 WHERE parent = %s AND item_code = %s
                #         #             """, (item_qty_is_scrap_item_aa, stock_entry.name, item_code_is_scrap_item_aa))
                #         #
                #         # frappe.db.commit()
                #         pass
                #
                #     else:
                #         frappe.db.set_value("Stock Entry Detail",
                #                             {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa},
                #                             "qty", result_qty_scrap_item)
                #
                #
                # #     # if result_qty_scrap_item >= item_qty_is_scrap_item_aa:
                # #     #     frappe.throw(_("Resulting quantity exceeds the scrap item quantity."))
                # else:
                #     frappe.throw(_("Ensure both the resulting quantity and scrap item quantity are numeric."))
    # else:
    #     pass



# ======= END Fetch Qty From Table Scrap Item in BOM  ===========
# ========================================================
# ========================================================









# ========================================================
# ========================================================








# ========================================================
# ========================================================
# =========  START Fetch Qty From Table Scrap Item in BOM -- No. 2 ==============


@frappe.whitelist()
def fetch_qty_from_table_scrap_item_in_bom_no_2(doc, method=None):

    # if not doc:
    #     frappe.throw(_("Document is required"))

    stock_entry = frappe.get_doc("Stock Entry", doc) if isinstance(doc, str) else doc

    # if stock_entry.docstatus == 0 and stock_entry.stock_entry_type == 'Manufacture':

    # bom_check_a_001

    bom_check_detail = frappe.get_all(
        "Stock Entry",
        filters={"name": stock_entry.name},
        fields=["bom_check_a_001", ],
    )

    bom_check_info = bom_check_detail[0].get('bom_check_a_001')

    # if bom_check_info == 1 or bom_check_info == 0:

    # frappe.db.set_value("Stock Entry", stock_entry.name, "bom_check_a_001", 0)

    # frappe.msgprint(str(bom_check_info))

    # if bom_check_detail:
    #     bom_check_info = bom_check_detail[0].get('bom_check_a_001')

    if bom_check_info == 1:
        stock_entry_items = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": stock_entry.name},
            fields=[
                "name", "item_code", "qty", "uom", "is_finished_item", "is_scrap_item",
                "basic_rate", "bom_no", "item_name", "t_warehouse"
            ]
        )

        bom_no = stock_entry.bom_no
        if not bom_no:
            frappe.throw(_("BOM is not linked with this Stock Entry"))

        bom_fetch_total_cost = frappe.get_all(
            "BOM",
            filters={"name": bom_no},
            fields=["total_cost"]
        )

        # if not bom_fetch_total_cost:
        #     frappe.throw(_("BOM Total Cost not found."))
        #
        # bom_total_cost = bom_fetch_total_cost[0].get('total_cost')

        bom_fetch_bom_scrap_item = frappe.get_all(
            "BOM Scrap Item",
            filters={"parent": bom_no},
            fields=["item_code", "item_name", "stock_qty", "stock_uom", ]
        )

        bom_fetch_bom_scrap_item_qty = None

        # bom_fetch_bom_scrap_item_qty = [item["stock_qty"] for item in bom_fetch_bom_scrap_item if
        #                                 "stock_qty" in item]

        for stock_entry_item in stock_entry_items:
            for bom_scrap_item in bom_fetch_bom_scrap_item:
                if stock_entry_item["item_code"] == bom_scrap_item["item_code"]:
                    bom_fetch_bom_scrap_item_qty = bom_scrap_item.get("stock_qty", 0)

        # if bom_fetch_bom_scrap_item:
        #     bom_fetch_bom_scrap_item_qty = bom_fetch_bom_scrap_item[0].get("stock_qty")
        # else:
        #     bom_fetch_bom_scrap_item_qty = None

        for item_a in stock_entry_items:
            if item_a.get("is_scrap_item") == 1:
                item_code_is_scrap_item = item_a["item_code"]


        work_order = stock_entry.work_order
        if not work_order:
            frappe.throw(_("work_order is not linked with this Stock Entry"))

        work_order_fetch_info = frappe.get_all(
            "Work Order",
            filters={"name": work_order},
            fields=["actual_qty_to_manufacture_a_001"]
        )

        for work_order_item in work_order_fetch_info:
            work_order_fetch_actual_qty_to_manufacture_a_001 = work_order_item.get("actual_qty_to_manufacture_a_001", 0)


        # frappe.msgprint(str(item_code_is_scrap_item))
        # frappe.msgprint(str(bom_no))
        # frappe.msgprint(str(bom_fetch_total_cost))
        # frappe.msgprint(str(bom_fetch_bom_scrap_item))
        #
        # frappe.msgprint(str(bom_fetch_bom_scrap_item_qty), alert=True)
        # frappe.msgprint(str(work_order_fetch_actual_qty_to_manufacture_a_001), alert=True)


        # if isinstance(bom_fetch_bom_scrap_item_qty, (int, float)) and isinstance(
        #         work_order_fetch_actual_qty_to_manufacture_a_001, (int, float)):
        #     result_qty_scrap_item = bom_fetch_bom_scrap_item_qty * work_order_fetch_actual_qty_to_manufacture_a_001
        #     frappe.msgprint(str(result_qty_scrap_item))
        # else:
        #     frappe.throw(_("Ensure both quantities are numeric for calculation."))

        try:
            bom_fetch_bom_scrap_item_qty = float(bom_fetch_bom_scrap_item_qty)
            work_order_fetch_actual_qty_to_manufacture_a_001 = float(work_order_fetch_actual_qty_to_manufacture_a_001)

            result_qty_scrap_item = bom_fetch_bom_scrap_item_qty * work_order_fetch_actual_qty_to_manufacture_a_001
            # frappe.msgprint(_("Resulting Scrap Item Quantity: {0}").format(result_qty_scrap_item))

        except (TypeError, ValueError):
            frappe.throw(_("Ensure both quantities are numeric for calculation."))




        # if bom_fetch_bom_scrap_item_qty is None or work_order_fetch_actual_qty_to_manufacture_a_001 is None:
        #     frappe.throw(_("One or both of the required quantities are missing."))
        #
        # try:
        #     bom_fetch_bom_scrap_item_qty = float(bom_fetch_bom_scrap_item_qty)
        #     work_order_fetch_actual_qty_to_manufacture_a_001 = float(work_order_fetch_actual_qty_to_manufacture_a_001)
        #
        #     result_qty_scrap_item = bom_fetch_bom_scrap_item_qty * work_order_fetch_actual_qty_to_manufacture_a_001
        #     frappe.msgprint(_("Resulting Scrap Item Quantity: {0}").format(result_qty_scrap_item))
        #
        # except ValueError:
        #     frappe.throw(_("Ensure both quantities are numeric for calculation."))






        for item_aa in stock_entry_items:
            if item_aa.get("is_scrap_item") == 1:
                item_code_is_scrap_item_aa = item_aa["item_code"]
                item_qty_is_scrap_item_aa = item_aa["qty"]

                # frappe.msgprint(str(item_code_is_scrap_item_aa), alert=True)
                # frappe.msgprint(str(item_qty_is_scrap_item_aa), alert=True)




                if isinstance(result_qty_scrap_item, (int, float)) and isinstance(item_qty_is_scrap_item_aa,
                                                                                  (int, float)):


                    if item_qty_is_scrap_item_aa > result_qty_scrap_item:
                        # frappe.throw(_("Resulting quantity exceeds the scrap item quantity."))
                        frappe.db.set_value("Stock Entry Detail",
                                            {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa, "is_scrap_item": 1},
                                            "qty", result_qty_scrap_item)

                    elif item_qty_is_scrap_item_aa == result_qty_scrap_item:
                        frappe.db.set_value("Stock Entry Detail",
                                            {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa, "is_scrap_item": 1},
                                            "qty", result_qty_scrap_item)

                    elif item_qty_is_scrap_item_aa < result_qty_scrap_item:
                        frappe.db.set_value("Stock Entry Detail",
                                            {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa, "is_scrap_item": 1},
                                            "qty", item_qty_is_scrap_item_aa)

                        # # frappe.db.sql("""
                        # #                 UPDATE `tabStock Entry Detail`
                        # #                 SET qty = %s
                        # #                 WHERE parent = %s AND item_code = %s
                        # #             """, (item_qty_is_scrap_item_aa, stock_entry.name, item_code_is_scrap_item_aa))
                        # #
                        # # frappe.db.commit()
                        # pass

                    else:
                        frappe.db.set_value("Stock Entry Detail",
                                            {"parent": stock_entry.name, "item_code": item_code_is_scrap_item_aa, "is_scrap_item": 1},
                                            "qty", result_qty_scrap_item)


                #     # if result_qty_scrap_item >= item_qty_is_scrap_item_aa:
                #     #     frappe.throw(_("Resulting quantity exceeds the scrap item quantity."))
                else:
                    frappe.throw(_("Ensure both the resulting quantity and scrap item quantity are numeric."))
    # else:
    #     pass



# ======= END Fetch Qty From Table Scrap Item in BOM -- No. 2 ===========
# ========================================================
# ========================================================











# ========================================================
# ========================================================












# ========================================================
# ========================================================
# ========================================================
# ========================================================









