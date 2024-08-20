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





	],



//	"onload": function(report) {
//		report.page.add_inner_button(__('Show Work Order'), function() {
//            showStyledMessage();
//        });
//	}

    "onload": function(report) {
//        report.page.add_inner_button(__('Show Chart'), function() {
//            renderChart();
////            renderChart_a();
//        });
        report.page.add_inner_button(__('Show Table'), function() {
            renderTable();
//            renderChart()
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







////  ===============================
////  ===============================
//
//
//function loadScript(src, callback) {
//    var script = document.createElement('script');
//    script.src = src;
//    script.onload = callback;
//    script.onerror = function() {
//        console.error('Failed to load script:', src);
//    };
//    document.head.appendChild(script);
//}
//
//function renderChart() {
//    frappe.call({
//        method: 'elfadaly_test_001.elfadaly_test_001.report.analysis_of_standard_deviation.analysis_of_standard_deviation.get_work_order_data',
//        args: {
//            filters: JSON.stringify(frappe.query_report.get_filter_values())
//        },
//        callback: function(r) {
//            if (!r.exc) {
//                console.log('Data:', r.message);
//                const data = r.message;
//                const labels = data.map(row => row.work_order);
//                const processLossQty = data.map(row => row.process_loss_qty_wo);
//
//                const chartHtml = `
//                    <div style="text-align: center;">
//                        <canvas id="workOrderChart" width="600" height="400"></canvas>
//                    </div>
//                `;
//
//                const dialog = new frappe.ui.Dialog({
//                    title: __('Work Order Chart'),
//                    fields: [
//                        {
//                            fieldtype: 'HTML',
//                            fieldname: 'chart',
//                            options: chartHtml
//                        }
//                    ],
//                    onshow: function() {
//                        if (typeof Chart !== 'undefined') {
//                            const ctx = document.getElementById('workOrderChart').getContext('2d');
//                            if (ctx) {
//                                new Chart(ctx, {
//                                    type: 'bar',
//                                    data: {
//                                        labels: labels,
//                                        datasets: [{
//                                            label: 'Process Loss Quantity',
//                                            data: processLossQty,
//                                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
//                                            borderColor: 'rgba(75, 192, 192, 1)',
//                                            borderWidth: 1
//                                        }]
//                                    },
//                                    options: {
//                                        scales: {
//                                            y: {
//                                                beginAtZero: true
//                                            }
//                                        }
//                                    }
//                                });
//                            } else {
//                                console.error('Canvas element not found');
//                            }
//                        } else {
//                            console.error('Chart.js is not loaded');
//                        }
//                    }
//                });
//
//                dialog.show();
//            } else {
//                console.error(r.exc);
//            }
//        }
//    });
//}
//
//loadScript('https://cdn.jsdelivr.net/npm/chart.js', function() {
//    console.log('Chart.js loaded successfully');
//    renderChart();
//});
//
//
//
//
//
//
////  ===============================
////  ===============================






//  ===============================
//  ===============================





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



function renderChart() {
    const chartScript = document.createElement('script');
    chartScript.src = 'https://cdn.jsdelivr.net/npm/chart.js';
    document.head.appendChild(chartScript);

    chartScript.onload = function() {
        frappe.call({
            method: 'elfadaly_test_001.elfadaly_test_001.report.analysis_of_standard_deviation.analysis_of_standard_deviation.get_work_order_data',
            args: {
                filters: JSON.stringify(frappe.query_report.get_filter_values())
            },
            callback: function(r) {
                if (!r.exc) {
                    const data = r.message;

                    const workOrders = data.map(row => row.work_order);
                    const processLossQty = data.map(row => row.process_loss_qty_wo || 0);
                    const processLossDiffQty = data.map(row => row.process_loss_difference_qty || 0);

                    const dialogHtml = `
                        <canvas id="chart" width="400" height="200"></canvas>
                    `;

                    const dialog = new frappe.ui.Dialog({
                        title: __('Work Order Data Chart'),
                        fields: [
                            {
                                fieldtype: 'HTML',
                                fieldname: 'chart',
                                options: dialogHtml
                            }
                        ]
                    });

                    dialog.show();

                    dialog.on('show', function() {
                        const ctx = document.getElementById('chart').getContext('2d');
                        new Chart(ctx, {
                            type: 'bar',
                            data: {
                                labels: workOrders,
                                datasets: [
                                    {
                                        label: 'Process Loss Quantity',
                                        data: processLossQty,
                                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                                        borderColor: 'rgba(75, 192, 192, 1)',
                                        borderWidth: 1
                                    },
                                    {
                                        label: 'Process Loss Difference Quantity',
                                        data: processLossDiffQty,
                                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                                        borderColor: 'rgba(153, 102, 255, 1)',
                                        borderWidth: 1
                                    }
                                ]
                            },
                            options: {
                                scales: {
                                    x: {
                                        beginAtZero: true
                                    },
                                    y: {
                                        beginAtZero: true
                                    }
                                }
                            }
                        });
                    });
                } else {
                    console.error('Error:', r.exc);
                    frappe.msgprint(__('Failed to load data. Please try again.'));
                }
            }
        });
    };

    chartScript.onerror = function() {
        frappe.msgprint(__('Failed to load Chart.js. Please check your internet connection.'));
    };
}







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


















