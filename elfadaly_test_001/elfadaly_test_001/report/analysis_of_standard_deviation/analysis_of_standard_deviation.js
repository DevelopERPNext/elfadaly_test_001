// Copyright (c) 2024, khattab.info and contributors
// For license information, please see license.txt

frappe.query_reports["Analysis of Standard Deviation"] = {
	"filters": [
        {
            "fieldname": "date_from",
            "label": __("Date From"),
            "fieldtype": "Date",
            "reqd": 0,
            "width": "150px"
        },
        {
            "fieldname": "date_to",
            "label": __("Date To"),
            "fieldtype": "Date",
            "reqd": 0,
            "width": "150px"
        },

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


	],


    "onload": function(report) {
        report.page.add_inner_button(__('Show Table'), function() {
            renderTable();
        });


        report.page.add_inner_button(__('Clear Filters'), function() {
            report.set_filter_value('date_from', '');
            report.set_filter_value('date_to', '');
            report.set_filter_value('work_order', '');
            report.set_filter_value('item_code', '');
            report.refresh();
        });

    }

};




function renderChart_a() {
    frappe.call({
        method: 'elfadaly_test_001.elfadaly_test_001.report.analysis_of_standard_deviation.analysis_of_standard_deviation.test_method',
        callback: function(r) {
            if (!r.exc) {
                frappe.msgprint(r.message);
            } else {
                frappe.msgprint(r.exc);
            }
        }
    });
}





// -------- Working ------------


function renderTable() {
    frappe.call({
        method: 'elfadaly_test_001.elfadaly_test_001.report.analysis_of_standard_deviation.analysis_of_standard_deviation.get_work_order_data',
        args: {
            filters: JSON.stringify(frappe.query_report.get_filter_values())
        },
        callback: function(r) {
            if (!r.exc) {
                const data = r.message;
                console.log('Data:', data);

                let tableHtml = `
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>Work Order</th>
                                <th>Process Loss Quantity</th>
                                <th>Process Loss Difference Quantity</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                data.forEach(row => {
                    let style = '';
                    if (row.process_loss_qty_wo > 0) {
                        style = 'color: darkblue; font-weight: bold; font-size: 18px;';
                    }
                    tableHtml += `
                        <tr>
                            <td>${row.work_order}</td>
                            <td style="${style}">${row.process_loss_qty_wo}</td>
                            <td style="${style}">${row.process_loss_difference_qty}</td>
                        </tr>
                    `;
                });
                tableHtml += `
                        </tbody>
                    </table>
                `;

                const dialog = new frappe.ui.Dialog({
                    title: __('Work Order Data'),
                    fields: [
                        {
                            fieldtype: 'HTML',
                            fieldname: 'table',
                            options: tableHtml
                        }
                    ]
                });

                dialog.show();
            } else {
                console.error(r.exc);
            }
        }
    });
}




//   -----------------------------------





//  ===============================
//  ===============================



//<p>Date: ${currentDate}</p>



function showStyledMessage() {
    const currentDate = new Date().toLocaleDateString();

    const message = `
        <div style="font-weight: bold; color: blue;">
            <p>Date: ${currentDate}</p>
        </div>
    `;

    frappe.msgprint({
        title: __('Show Work Order'),
        message: message,
        indicator: 'blue'
    });
}







//  ===============================
//  ===============================
//  ===============================
//  ===============================





