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











