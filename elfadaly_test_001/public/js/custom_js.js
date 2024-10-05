// ==============================================================
// ================== Branch Purchase Order ================

frappe.listview_settings['Purchase Order'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Purchase Order", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Purchase Order", "branch_purchase_order_a_001", "=", default_branch]
            ]);
        }

//        listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
        listview.refresh();


//        listview.page.add_inner_button(__('Custom Action'), function() {
//            listview.filter_area.add([
//                ["Purchase Order", "owner", "=", frappe.session.user]
//            ]);
//            listview.refresh();
//        });

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Purchase Order', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_purchase_order_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------






// ==============================================================
// ================== Branch Purchase Invoice ================

frappe.listview_settings['Purchase Invoice'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Purchase Invoice", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Purchase Invoice", "branch_purchase_invoice_a_001", "=", default_branch]
            ]);
        }

        listview.refresh();

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Purchase Invoice', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_purchase_invoice_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------





// ==============================================================
// ================== Branch Sales Order ================

frappe.listview_settings['Sales Order'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Sales Order", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Sales Order", "branch_sales_order_a_001", "=", default_branch]
            ]);
        }

        listview.refresh();

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Sales Order', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_sales_order_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------



// ==============================================================
// ================== Branch Sales Invoice ================

frappe.listview_settings['Sales Invoice'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Sales Invoice", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Sales Invoice", "branch_sales_invoice_a_001", "=", default_branch]
            ]);
        }

        listview.refresh();

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Sales Invoice', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_sales_invoice_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------



// ==============================================================
// ================== Branch Purchase Receipt ================

frappe.listview_settings['Purchase Receipt'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Purchase Receipt", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Purchase Receipt", "branch_purchase_receipt_a_001", "=", default_branch]
            ]);
        }

        listview.refresh();

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Purchase Receipt', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_purchase_receipt_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------


// ==============================================================
// ================== Branch Delivery Note ================

frappe.listview_settings['Delivery Note'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Delivery Note", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Delivery Note", "branch_delivery_note_a_001", "=", default_branch]
            ]);
        }

        listview.refresh();

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Delivery Note', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_delivery_note_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------





// ==============================================================
// ================== Branch Stock Entry ================

frappe.listview_settings['Stock Entry'] = {
    onload: function(listview) {
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        if (default_company) {
            listview.filter_area.add([
                ["Stock Entry", "company", "=", default_company]
            ]);
        }

        if (default_branch) {
            listview.filter_area.add([
                ["Stock Entry", "branch_stock_entry_a_001", "=", default_branch]
            ]);
        }

        listview.refresh();

        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
            listview.refresh();
        });
    }
};


// ==============================================================

frappe.ui.form.on('Stock Entry', {
    onload: function(frm) {
        let default_branch = frappe.defaults.get_default("branch");

        if (default_branch) {
            frm.set_value('branch_stock_entry_a_001', default_branch);
        }
    }
});


// ==============================================================



// ----------------------------------------------------------------



















// ---------------------------------------------------------------
// ---------------------------------------------------------------
// ---------------------------------------------------------------



////  Filter by User - Purchase Receipt
//
//frappe.listview_settings['Purchase Receipt'] = {
//    onload: function(listview) {
//        if (frappe.session.user !== 'Administrator') {
//            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
//            listview.refresh();
//
//            listview.page.add_inner_button(__('Filter by User'), function() {
//                listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
//                listview.refresh();
//            });
//        }
//    }
//};


// **********************************


////  Display Finished Items - 2
//
//frappe.ui.form.on('Stock Entry', {
//    onload: function(frm) {
//        const currentUser = frappe.session.user;
//
//        // Automatically filter items if the current user is 'stock@elfadaly.com'
//        if (currentUser === 'stock@elfadaly.com' && frm.doc.stock_entry_type === 'Manufacture') {
//            frm.fields_dict['items'].grid.get_data().forEach(function(row) {
//                if (!row.is_finished_item) {
//                    frappe.model.clear_doc(row.doctype, row.name);
//                }
//            });
//            frm.fields_dict['items'].grid.refresh();
//        }
//
//
//    },
//
//
//    refresh: function(frm) {
//        // Add a custom button to manually filter finished items
//            frm.add_custom_button(__('Show Finished Items'), function() {
//                if (frm.doc.stock_entry_type === 'Manufacture') {
//                    frm.fields_dict['items'].grid.get_data().forEach(function(row) {
//                        if (!row.is_finished_item) {
//                            frappe.model.clear_doc(row.doctype, row.name);
//                        }
//                    });
//                    frm.fields_dict['items'].grid.refresh();
//                }
//
//        });
//    },
//
//});


// **********************************



////  Filter by User - Stock Entry Type : Material Transfer - 5
//
//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        const currentUser = frappe.session.user;
//
//        if (currentUser === 'manufacturing@elfadaly.com' || currentUser === 'Administrator') {
//            listview.filter_area.add([
//                [listview.doctype, 'stock_entry_type', 'in', ['Material Transfer for Manufacture']]
//            ]);
//            listview.refresh();
//        } else {
//            listview.no_result_message = __('You do not have permission to view these entries. ==');
//            listview.render_list([]);
//
//            // hide the entire filter button group if the user does not have permission
//            $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button').closest('.btn-group').hide();
//        }
//
//        listview.page.add_inner_button(__('Filter by User'), function() {
//            listview.filter_area.add([[listview.doctype, 'owner', '=', currentUser]]);
//
//            if (currentUser !== 'manufacturing@elfadaly.com' && currentUser !== 'Administrator') {
//                listview.filter_area.add([
//                    // [listview.doctype, 'stock_entry_type', 'not in', ['Manufacture', 'Material Transfer for Manufacture']]
//                    [listview.doctype, 'stock_entry_type', 'not in', ['Material Transfer for Manufacture']]
//                ]);
//            }
//
//            listview.refresh();
//        });
//    }
//};



// **********************************


////  Attendance Rules Configuration - 2
//
//frappe.ui.form.on('Employee Checkin', {
//    validate: function(frm) {
//        // Ensure 'log_type' is 'IN' and check if the 'time' field is filled
//        if (frm.doc.log_type === 'IN' && frm.doc.time) {
//
//            // Set the shift start time to the same date as the check-in time
//            let checkin_date = moment(frm.doc.time, 'YYYY-MM-DD HH:mm:ss').format('YYYY-MM-DD');
//            let shift_start_time = moment(checkin_date + ' 08:00:00', 'YYYY-MM-DD HH:mm:ss');
//            let checkin_time = moment(frm.doc.time, 'YYYY-MM-DD HH:mm:ss');
//
//            // Calculate the difference in minutes between shift start and check-in time
//            let late_minutes = checkin_time.diff(shift_start_time, 'minutes');
//
//            // Check if the employee is late and apply the penalty logic
//            if (late_minutes > 20 && late_minutes <= 80) {
//                frm.set_value('custom_late_entry', '1/4 Day');
//            } else if (late_minutes > 80 && late_minutes <= 120) {
//                frm.set_value('custom_late_entry', '1/2 Day');
//            } else if (late_minutes > 120) {
//                frm.set_value('custom_late_entry', 'Full Day');
//            } else {
//                frm.set_value('custom_late_entry', 'On Time'); // If on time or early
//            }
//        }
//    }
//});


// **********************************
// **********************************





// ==============================================================
// ==============================================================
// ==============================================================





