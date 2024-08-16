// Copyright (c) 2024, khattab.info and contributors
// For license information, please see license.txt

frappe.query_reports["Analysis of Standard Deviation"] = {
	"filters": [


        {
			"fieldname": "work_order",
			"label": __("Work Order"),
			"fieldtype": "Link",
			"options": "Work Order",
			"reqd": 0,
			"width": "200px"
		},
		{
			"fieldname": "item_code",
			"label": __("Item Code"),
			"fieldtype": "Link",
			"options": "Item",
			"reqd": 0,
			"width": "200px"
		}





	]
};
