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
        // Fetch user roles
        frappe.call({
            method: "elfadaly_test_001.elfadaly_test_001.custom.get_user_roles_a",
            callback: function(response) {
                if (response.message) {
                    const user_roles = response.message;
                    const filterButtons = $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button').closest('.btn-group');

                    // Show filter buttons if the user is Administrator or does not have المخازن role
                    if (frappe.session.user === 'Administrator' || !user_roles.includes("المخازن")) {
                        filterButtons.show();
                    } else {
                        filterButtons.hide();
                    }
                }
            },
            error: function(error) {
                frappe.msgprint(__('Error fetching roles: ') + error.message);
                console.error("Error fetching roles:", error);
            }
        });

        // Fetch default company and branch settings
        let default_company = frappe.defaults.get_default("company");
        let default_branch = frappe.defaults.get_default("branch");

        // Apply default company and branch filters if they exist
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

        // Add a custom button to filter by the current user
        listview.page.add_inner_button(__('Filter by User'), function() {
            listview.filter_area.clear();

            // Adding filter for owner and modified by
            listview.filter_area.add([
                ["Stock Entry", "owner", "=", frappe.session.user],
                ["Stock Entry", "modified_by", "=", frappe.session.user]
            ]);

            // Add default filters again
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
        });
    }
};






//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        // Fetch default company and branch settings
//        let default_company = frappe.defaults.get_default("company");
//        let default_branch = frappe.defaults.get_default("branch");
//
//        // Apply default company and branch filters if they exist
//        if (default_company) {
//            listview.filter_area.add([
//                ["Stock Entry", "company", "=", default_company]
//            ]);
//        }
//        if (default_branch) {
//            listview.filter_area.add([
//                ["Stock Entry", "branch_stock_entry_a_001", "=", default_branch]
//            ]);
//        }
//
//        // Add a custom button to filter by the current user
//        listview.page.add_inner_button(__('Filter by User'), function() {
//            listview.filter_area.clear();
//            listview.filter_area.add([
//                ["Stock Entry", "owner", "=", frappe.session.user]
//            ]);
//            listview.refresh();
//        });
//
////        // Check if the current user has the "المخازن" role
////        if (frappe.user.has_role("المخازن")) {
////            // Hide filter button group if user has "المخازن" role
////            $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button')
////                .closest('.btn-group').hide();
////        }
//
//
//    }
//};


// ------------------------------------

//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        // Delay to ensure buttons are rendered
//        setTimeout(function() {
//            // Check if the current user has the "المخازن" role
//            if (frappe.user.has_role("المخازن")) {
//                // Hide filter button group if user has "المخازن" role
//                $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button')
//                    .closest('.btn-group').hide();
//            } else {
//                // Show filter button group if user does not have the "المخازن" role
//                $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button')
//                    .closest('.btn-group').show();
//            }
//        }, 500);  // Adjust the delay as needed
//    }
//};

// ---------------------------------------

//// **********************************
//
//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        frappe.call({
//            method: "elfadaly_test_001.elfadaly_test_001.custom.get_user_roles_a",
//            callback: function(response) {
//                if (response.message) {
//                    const user_roles = response.message;
//                    const filterButtons = $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button').closest('.btn-group');
//
//                    // Show filter buttons if the user is Administrator or does not have المخازن role
//                    if (frappe.session.user === 'Administrator' || !user_roles.includes("المخازن")) {
//                        filterButtons.show();
//                        // frappe.msgprint(__('User is Administrator or does not have المخازن role: Showing filter buttons.'));
//                    } else {
//                        filterButtons.hide();
//                        if (user_roles.includes("المخازن")) {
////                            frappe.msgprint(__('User has المخازن role: Hiding filter buttons.'));
//                        }
//                    }
//                } else {
//                    // frappe.msgprint(__('No roles found for current user.'));
//                }
//            },
//            error: function(error) {
//                frappe.msgprint(__('Error fetching roles: ') + error.message);
//                console.error("Error fetching roles:", error);
//            }
//        });
//    }
//};








//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        frappe.call({
//            method: "elfadaly_test_001.elfadaly_test_001.custom.get_user_roles_a",
//            callback: function(response) {
//                if (response.message) {
//                    const user_roles = response.message;
//                    const filterButtons = $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button').closest('.btn-group');
//
//                    if (user_roles.includes("المخازن")) {
//                        filterButtons.hide();
//                        frappe.msgprint(__('User has المخازن role: Hiding filter buttons.'));
//                    } else {
//                        filterButtons.show();
//                        frappe.msgprint(__('User does not have المخازن role: Showing filter buttons.'));
//                    }
//                } else {
//                    frappe.msgprint(__('No roles found for current user.'));
//                }
//            },
//            error: function(error) {
//                frappe.msgprint(__('Error fetching roles: ') + error.message);
//                console.error("Error fetching roles:", error);
//            }
//        });
//    }
//};









//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        const filterButtons = $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button').closest('.btn-group');
//
//        if (frappe.user.has_role("المخازن")) {
//            filterButtons.hide();
//        } else {
//            filterButtons.show();
//        }
//    }
//};






//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        frappe.call({
//            method: "elfadaly_test_001.elfadaly_test_001.custom.get_user_roles_a",
//            callback: function(response) {
//                if (response.message) {
//                    const user_roles = response.message;
//                    if (user_roles.length > 0) {
//                        frappe.msgprint(__('Roles for current user: ') + user_roles.join(', '));
//                        console.log("User Roles:", user_roles);
//                    } else {
//                        frappe.msgprint(__('No roles found for current user.'));
//                        console.log("No roles found for current user.");
//                    }
//                } else {
//                    frappe.msgprint(__('No roles found for current user.'));
//                }
//            },
//            error: function(error) {
//                frappe.msgprint(__('Error fetching roles: ') + error.message);
//                console.error("Error fetching roles:", error);
//            }
//        });
//    }
//};














// -----------------------------------------------

//frappe.listview_settings['Stock Entry'] = {
//    onload: function(listview) {
//        let default_company = frappe.defaults.get_default("company");
//        let default_branch = frappe.defaults.get_default("branch");
//        let currentUser = frappe.session.user; // Get the current user
//
//        if (default_company) {
//            listview.filter_area.add([
//                ["Stock Entry", "company", "=", default_company]
//            ]);
//        }
//
//        if (default_branch) {
//            listview.filter_area.add([
//                ["Stock Entry", "branch_stock_entry_a_001", "=", default_branch]
//            ]);
//        }
//
//        listview.refresh();
//
//        listview.page.add_inner_button(__('Filter by User'), function() {
//            listview.filter_area.clear();
//            listview.filter_area.add([[listview.doctype, 'owner', '=', frappe.session.user]]);
//            listview.refresh();
//        });
//
//        // Check if the current user matches the specified email
//        if (currentUser === 'stock_1@khattab.info') {
//            // Hide the filter button group
//            $('.btn-group .btn.filter-button, .btn-group .btn.filter-x-button').closest('.btn-group').hide();
//            listview.refresh();
//        }
//    }
//};









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





// ==============================================================
// ================== Branch Stock Entry ================



//frappe.ui.form.on("Stock Entry", {
//    refresh: function(frm) {
//        if (frm.doc.stock_entry_type === "Material Transfer" && frm.doc.docstatus === 0) {
//            // If the user's branch is different from the receiving branch, show a custom button
//            if (frm.doc.branch !== frm.doc.branch_receiving_branch_a_001) {
//                frm.add_custom_button("Save for Receiving Branch", function() {
//                    frappe.msgprint("The document has been saved and will be processed by the receiving branch.");
//                });
//            }
//        }
//    }
//});



// ==============================================================



// ----------------------------------------------------------------







// ==============================================================
// ================== actual_qty_to_manufacture_a_001 ================


// JavaScript function to perform the calculation and update the qty field in Work Order


frappe.ui.form.on('Work Order', {
    actual_qty_to_manufacture_a_001: function(frm) {
        frappe.call({
            method: "elfadaly_test_001.elfadaly_test_001.custom.calculate_qty",
            args: {
                work_order_name: frm.doc.name,
                actual_qty: frm.doc.actual_qty_to_manufacture_a_001,
                bom_no: frm.doc.bom_no
            },
            callback: function(response) {
                if (response.message) {
                    frm.set_value("qty", response.message);
                    frm.refresh_field("qty");
                }
            }
        });
    }
});


// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------



// ================================================================================
// ========================== START Hidden Price ==================================



// ==============================================================
// ================== (BOM) The Hidden Price Fields in the Doctype -- a_001  ================


frappe.ui.form.on('BOM', {
    onload_post_render: function(frm) {
        hideBOMFields(frm);
        hideItemFields(frm);
    },

    onload: function(frm) {
        hideBOMFields(frm);
        hideItemFields(frm);
    },

    refresh: function(frm) {
        hideBOMFields(frm);
        hideItemFields(frm);
    },

    setup: function(frm, cdt, cdn) {
        hideItemFields(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hideItemFields(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hideItemFields(frm);
    },

    on_save: function(frm) {
        hideItemFields(frm);
    },

    after_save: function(frm) {
        hideItemFields(frm);
    },

    on_submit: function(frm) {
        hideItemFields(frm);
    }

});

function hideBOMFields(frm) {
    // Hide specific single fields
    frm.set_df_property('costing', 'hidden', 1);
    frm.set_df_property('more_info_tab', 'hidden', 1);
    frm.set_df_property('operating_cost', 'hidden', 1);
    frm.set_df_property('raw_material_cost', 'hidden', 1);
    frm.set_df_property('scrap_material_cost', 'hidden', 1);
    frm.set_df_property('base_operating_cost', 'hidden', 1);
    frm.set_df_property('base_raw_material_cost', 'hidden', 1);
    frm.set_df_property('base_scrap_material_cost', 'hidden', 1);
    frm.set_df_property('total_cost', 'hidden', 1);
    frm.set_df_property('base_total_cost', 'hidden', 1);
    frm.set_df_property('exploded_items', 'hidden', 1);
}

function hideItemFields(frm) {
    // Toggle display for specific fields in the items grid
    frm.fields_dict['items'].grid.toggle_display('rate_amount_section', false);
    frm.fields_dict['items'].grid.toggle_display('rate', false);
    frm.fields_dict['items'].grid.toggle_display('amount', false);


    frm.fields_dict['operations'].grid.toggle_display('costing_section', false);

//    // Set the visibility of fields in the list view
//    frm.fields_dict['items'].grid.set_column_disp('rate', false);
//    frm.fields_dict['items'].grid.set_column_disp('amount', false);


//    // Hide specific fields from the list view in the child table
    frm.fields_dict['items'].grid.get_docfield('rate').in_list_view = 0;
    frm.fields_dict['items'].grid.get_docfield('amount').in_list_view = 0;


    frm.fields_dict['operations'].grid.get_docfield('operating_cost').in_list_view = 0;

    // Refresh the items grid to apply changes
    frm.fields_dict['items'].grid.refresh();
    frm.fields_dict['operations'].grid.refresh();

}


// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------





// ==============================================================
// ================== (Workstation) The Hidden Price Fields in the Doctype -- a_002  ================


frappe.ui.form.on('Workstation', {
    onload_post_render: function(frm) {
        hideWorkstationFields(frm);
    },

    onload: function(frm) {
        hideWorkstationFields(frm);
    },

    refresh: function(frm) {
        hideWorkstationFields(frm);
    },

    setup: function(frm, cdt, cdn) {
        hideWorkstationFields(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hideWorkstationFields(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hideWorkstationFields(frm);
    },

    on_save: function(frm) {
        hideWorkstationFields(frm);
    },


    after_save: function(frm) {
        hideWorkstationFields(frm);
    },

    on_submit: function(frm) {
        hideWorkstationFields(frm);
    }

});

function hideWorkstationFields(frm) {
    // Hide specific single fields
    frm.set_df_property('over_heads', 'hidden', 1);
    frm.set_df_property('hour_rate_electricity', 'hidden', 1);
    frm.set_df_property('hour_rate_consumable', 'hidden', 1);
    frm.set_df_property('hour_rate_rent', 'hidden', 1);
    frm.set_df_property('hour_rate_labour', 'hidden', 1);
    frm.set_df_property('hour_rate', 'hidden', 1);
}



// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------



// ==============================================================
// ================== (Routing) The Hidden Price Fields in the Doctype -- a_003  ================


frappe.ui.form.on('Routing', {
    onload_post_render: function(frm) {
        hideRoutingFields(frm);
    },

    onload: function(frm) {
        hideRoutingFields(frm);
    },

    refresh: function(frm) {
        hideRoutingFields(frm);
    },

    setup: function(frm, cdt, cdn) {
        hideRoutingFields(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hideRoutingFields(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hideRoutingFields(frm);
    },

    on_save: function(frm) {
        hideRoutingFields(frm);
    },

    after_save: function(frm) {
        hideRoutingFields(frm);
    },

    on_submit: function(frm) {
        hideRoutingFields(frm);
    }

});


function hideRoutingFields(frm) {
    // Toggle display for specific fields in the items grid
    frm.fields_dict['operations'].grid.toggle_display('costing_section', false);

    // Hide specific fields from the list view in the child table
    frm.fields_dict['operations'].grid.get_docfield('operating_cost').in_list_view = 0;

    // Refresh the items grid to apply changes
    frm.fields_dict['operations'].grid.refresh();

}



// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------




// ==============================================================
// ================== (Work Order) The Hidden Price Fields in the Doctype -- a_004  ================


frappe.ui.form.on('Work Order', {
    onload_post_render: function(frm) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    onload: function(frm) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    refresh: function(frm) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    setup: function(frm, cdt, cdn) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    on_save: function(frm) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },


    after_save: function(frm) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    },

    on_submit: function(frm) {
        hideWorkOrderFields(frm);
        hideItemFields_WO(frm);
    }

});


function hideWorkOrderFields(frm) {
    // Hide specific single fields
    frm.set_df_property('planned_operating_cost', 'hidden', 1);
    frm.set_df_property('actual_operating_cost', 'hidden', 1);
    frm.set_df_property('additional_operating_cost', 'hidden', 1);
    frm.set_df_property('corrective_operation_cost', 'hidden', 1);
    frm.set_df_property('total_operating_cost', 'hidden', 1);
}


function hideItemFields_WO(frm) {
    // Toggle display for specific fields in the items grid
    frm.fields_dict['required_items'].grid.toggle_display('rate', false);
    frm.fields_dict['required_items'].grid.toggle_display('amount', false);

    frm.fields_dict['operations'].grid.toggle_display('hour_rate', false);
    frm.fields_dict['operations'].grid.toggle_display('planned_operating_cost', false);
    frm.fields_dict['operations'].grid.toggle_display('actual_operating_cost', false);

//    // Hide specific fields from the list view in the child table
//    frm.fields_dict['required_items'].grid.get_docfield('operating_cost').in_list_view = 0;

    // Refresh the items grid to apply changes
    frm.fields_dict['required_items'].grid.refresh();
    frm.fields_dict['operations'].grid.refresh();

}



// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------







// ==============================================================
// ================== (Purchase Receipt) The Hidden Price Fields in the Doctype -- a_005  ================


frappe.ui.form.on('Purchase Receipt', {
    onload_post_render: function(frm) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    onload: function(frm) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    refresh: function(frm) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    setup: function(frm, cdt, cdn) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    on_save: function(frm) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    after_save: function(frm) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    },

    on_submit: function(frm) {
        hidePurchaseReceiptFields(frm);
        hideItemFields_PR(frm);
    }

});


function hidePurchaseReceiptFields(frm) {
    // Hide specific single fields
    frm.set_df_property('accounting_dimensions_section', 'hidden', 1);
    frm.set_df_property('currency_and_price_list', 'hidden', 1);
    frm.set_df_property('total', 'hidden', 1);
    frm.set_df_property('base_total', 'hidden', 1);
    frm.set_df_property('base_net_total', 'hidden', 1);
    frm.set_df_property('net_total', 'hidden', 1);
    frm.set_df_property('tax_withholding_net_total', 'hidden', 1);
    frm.set_df_property('base_tax_withholding_net_total', 'hidden', 1);
    frm.set_df_property('taxes_charges_section', 'hidden', 1);
    frm.set_df_property('taxes', 'hidden', 1);
    frm.set_df_property('totals', 'hidden', 1);
    frm.set_df_property('section_break_46', 'hidden', 1);
    frm.set_df_property('section_break_42', 'hidden', 1);
    frm.set_df_property('sec_tax_breakup', 'hidden', 1);
    frm.set_df_property('pricing_rule_details', 'hidden', 1);

    frm.set_df_property('more_info_tab', 'hidden', 1);

    frm.$wrapper.find('[data-fieldname="more_info_tab"]').hide();

}


function hideItemFields_PR(frm) {
    // Toggle display for specific fields in the items grid
    frm.fields_dict['items'].grid.toggle_display('sec_break1', false);
    frm.fields_dict['items'].grid.toggle_display('section_break_29', false);
    frm.fields_dict['items'].grid.toggle_display('rate_and_amount', false);
    frm.fields_dict['items'].grid.toggle_display('discount_and_margin_section', false);
    frm.fields_dict['items'].grid.toggle_display('accounting_details_section', false);


//    // Hide specific fields from the list view in the child table
    frm.fields_dict['items'].grid.get_docfield('rate').in_list_view = 0;
    frm.fields_dict['items'].grid.get_docfield('amount').in_list_view = 0;
    frm.fields_dict['items'].grid.get_docfield('net_amount').in_list_view = 0;

    // Refresh the items grid to apply changes
    frm.fields_dict['items'].grid.refresh();

}



// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------





// ==============================================================
// ================== (Delivery Note) The Hidden Price Fields in the Doctype -- a_006  ================


frappe.ui.form.on('Delivery Note', {
    onload_post_render: function(frm) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    onload: function(frm) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    refresh: function(frm) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    setup: function(frm, cdt, cdn) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    on_save: function(frm) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    after_save: function(frm) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    },

    on_submit: function(frm) {
        hideDeliveryNotetFields(frm);
        hideItemFields_DN(frm);
    }

});


function hideDeliveryNotetFields(frm) {
    // Hide specific single fields
    frm.set_df_property('accounting_dimensions_section', 'hidden', 1);
    frm.set_df_property('currency_and_price_list', 'hidden', 1);
    frm.set_df_property('base_total', 'hidden', 1);
    frm.set_df_property('base_net_total', 'hidden', 1);
    frm.set_df_property('total', 'hidden', 1);
    frm.set_df_property('net_total', 'hidden', 1);
    frm.set_df_property('taxes_section', 'hidden', 1);
    frm.set_df_property('taxes', 'hidden', 1);
    frm.set_df_property('section_break_44', 'hidden', 1);
    frm.set_df_property('totals', 'hidden', 1);
    frm.set_df_property('section_break_49', 'hidden', 1);
    frm.set_df_property('sec_tax_breakup', 'hidden', 1);
    frm.set_df_property('pricing_rule_details', 'hidden', 1);


    frm.$wrapper.find('[data-fieldname="more_info_tab"]').hide();

}


function hideItemFields_DN(frm) {
    // Toggle display for specific fields in the items grid
    frm.fields_dict['items'].grid.toggle_display('section_break_17', false);
    frm.fields_dict['items'].grid.toggle_display('discount_and_margin', false);
    frm.fields_dict['items'].grid.toggle_display('section_break_1', false);
    frm.fields_dict['items'].grid.toggle_display('section_break_25', false);
    frm.fields_dict['items'].grid.toggle_display('accounting_details_section', false);


//    // Hide specific fields from the list view in the child table
    frm.fields_dict['items'].grid.get_docfield('rate').in_list_view = 0;
    frm.fields_dict['items'].grid.get_docfield('amount').in_list_view = 0;

    // Refresh the items grid to apply changes
    frm.fields_dict['items'].grid.refresh();

}



// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------






// ==============================================================
// ================== (Stock Entry) The Hidden Price Fields in the Doctype -- a_007  ================


frappe.ui.form.on('Stock Entry', {
    onload_post_render: function(frm) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    onload: function(frm) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    refresh: function(frm) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    setup: function(frm, cdt, cdn) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    before_load: function(frm, cdt, cdn) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    form_render: function(frm, cdt, cdn) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    on_save: function(frm) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    after_save: function(frm) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    },

    on_submit: function(frm) {
        hideStockEntryFields(frm);
        hideItemFields_SE(frm);
    }

});


function hideStockEntryFields(frm) {
    // Hide specific single fields
    frm.set_df_property('section_break_19', 'hidden', 1);


    frm.$wrapper.find('[data-fieldname="other_info_tab"]').hide();

}


function hideItemFields_SE(frm) {
    // Toggle display for specific fields in the items grid
    frm.fields_dict['items'].grid.toggle_display('rates_section', false);
    frm.fields_dict['items'].grid.toggle_display('accounting', false);

    frm.fields_dict['items'].grid.toggle_display('basic_rate', false);


//    // Hide specific fields from the list view in the child table
    frm.fields_dict['items'].grid.get_docfield('basic_rate').in_list_view = 0;

    // Refresh the items grid to apply changes
    frm.fields_dict['items'].grid.refresh();

}



// ==============================================================
// ==============================================================

// --------------------------------------------------------------
// --------------------------------------------------------------



// ========================== END Hidden Price ==================================
// ==============================================================================






//   ================================================================
//   ================================================================
//   ==== START Batch Number Series cannot contain spaces ====


frappe.ui.form.on('Item', {
    validate: function(frm) {
        let batch_number_series = frm.doc.batch_number_series;

        if (batch_number_series && batch_number_series.includes(' ')) {
            frappe.show_alert({
                            message: __("Batch Number Series cannot contain spaces"),
                            indicator: 'red'
            });

            frappe.validated = false;
        }
    }
});


//   ==== END Batch Number Series cannot contain spaces ====
//   ================================================================
//   ================================================================








//   ================================================================
//   ================================================================
//   ==== START  Fetch the corresponding cost center number from Cost Center doctype (Sales Invoice) ====


frappe.ui.form.on('Sales Invoice', {
    after_save(frm) {
        // Flag to track if the invoice needs saving after updates
        let needsSave = false;

        // Loop through each item in the Sales Invoice
        frm.doc.items.forEach(item => {
            // Check if item_code is set
            if (item.item_code) {
                // Fetch the corresponding Cost Center name based on the item_code
                frappe.db.get_value('Cost Center', {'cost_center_number': item.item_code}, 'name')
                    .then(r => {
                        if (r.message && r.message.name) {
                            let cost_center_name = r.message.name;

                            // Set the cost_center field with the fetched Cost Center name
                            frappe.model.set_value(item.doctype, item.name, 'cost_center', cost_center_name);
                            needsSave = true; // Set flag to true if cost center is updated
                        } else {
                            // If no matching Cost Center is found, fetch the cost_center for the company
                            frappe.db.get_value('Company', frm.doc.company, 'cost_center') // Fetching 'cost_center' field from Company
                                .then(company => {
                                    if (company.message && company.message.cost_center) {
                                        let default_cost_center_name = company.message.cost_center;

                                        // Set the cost_center field to the fetched cost_center from Company
                                        frappe.model.set_value(item.doctype, item.name, 'cost_center', default_cost_center_name);
                                        needsSave = true; // Set flag to true if default cost center is used
                                    } else {
                                        frappe.msgprint(__('No Cost Center found for the company.'));
                                    }
                                })
                                .catch(err => {
                                    frappe.msgprint(__('Error fetching cost_center from Company: ') + err);
                                });
                        }
                    })
                    .catch(err => {
                        frappe.msgprint(__('Error fetching Cost Center: ') + err);
                    });
            }
        });

        // Check if any updates were made, if so, save the invoice
        if (needsSave) {
            frm.save();
        }

        // Refresh the items table to reflect the changes
        frm.refresh_field('items');
    }
});



//   ==== END Fetch the corresponding cost center number from Cost Center doctype (Sales Invoice)  ====
//   ================================================================
//   ================================================================








//   ================================================================
//   ================================================================
//   ==== START  Fetch the corresponding cost center number from Cost Center doctype (POS Invoice) ====



frappe.ui.form.on('POS Invoice', {
//    after_save(frm) {
    before_save(frm) {
//    validate(frm) {
        // Flag to track if the invoice needs saving after updates
        let needsSave = false;

        // Loop through each item in the Sales Invoice
        frm.doc.items.forEach(item => {
            // Check if item_code is set
            if (item.item_code) {
                // Fetch the corresponding Cost Center name based on the item_code
                frappe.db.get_value('Cost Center', {'cost_center_number': item.item_code}, 'name')
                    .then(r => {
                        if (r.message && r.message.name) {
                            let cost_center_name = r.message.name;

                            // Set the cost_center field with the fetched Cost Center name
                            frappe.model.set_value(item.doctype, item.name, 'cost_center', cost_center_name);
                            needsSave = true; // Set flag to true if cost center is updated
                        } else {
                            // If no matching Cost Center is found, fetch the cost_center for the company
                            frappe.db.get_value('Company', frm.doc.company, 'cost_center') // Fetching 'cost_center' field from Company
                                .then(company => {
                                    if (company.message && company.message.cost_center) {
                                        let default_cost_center_name = company.message.cost_center;

                                        // Set the cost_center field to the fetched cost_center from Company
                                        frappe.model.set_value(item.doctype, item.name, 'cost_center', default_cost_center_name);
                                        needsSave = true; // Set flag to true if default cost center is used
                                    } else {
                                        frappe.msgprint(__('No Cost Center found for the company.'));
                                    }
                                })
                                .catch(err => {
                                    frappe.msgprint(__('Error fetching cost_center from Company: ') + err);
                                });
                        }
                    })
                    .catch(err => {
                        frappe.msgprint(__('Error fetching Cost Center: ') + err);
                    });
            }
        });

        // Check if any updates were made, if so, save the invoice
        if (needsSave) {
            frm.save();
        }

        // Refresh the items table to reflect the changes
        frm.refresh_field('items');
    }
});



//   ==== END Fetch the corresponding cost center number from Cost Center doctype (POS Invoice)  ====
//   ================================================================
//   ================================================================





//   ================================================================
//   ================================================================
//   ==== START  Full payment is required to complete the invoice (POS Invoice) ====




frappe.ui.form.on('POS Invoice', {
	    validate: function(frm) {
            if (frm.doc.is_pos) {
                if (frm.doc.paid_amount < frm.doc.grand_total) {
                    // frappe.throw(__('Full payment is required to complete the invoice.'));
                    frappe.throw(__('يجب سداد المبلغ كاملا لاستكمال الفاتورة.'));
                }
                // if (frm.doc.paid_amount > frm.doc.grand_total) {
                //     // frappe.throw(__('The paid amount exceeds the total. Please return the excess.'));
                //     frappe.throw(__('المبلغ المدفوع يتجاوز المبلغ الإجمالي، يرجى إرجاع المبلغ الزائد.'));
                // }
            }
    }
});





//   ==== END  Full payment is required to complete the invoice (POS Invoice)  ====
//   ================================================================
//   ================================================================

























// ---------------------------------------------------------------
// ---------------------------------------------------------------
// ---------------------------------------------------------------


// ---------------------------------------------------------------
// ---------------------------------------------------------------
// ---------------------------------------------------------------


// ---------------------------------------------------------------
// ---------------------------------------------------------------
// ---------------------------------------------------------------



// ================================================================================
// ====================== START Reference Code ====================================



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


////Display Finished Items - 2
//
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
// **********************************


////Filter by User - Stock Entry Type : Material Transfer - 5
//
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
// **********************************


////The Hidden Price Fields in the Doctype -- a_001
//
//
//frappe.ui.form.on('Purchase Receipt', {
//    onload: function(frm) {
//        frm.set_df_property('currency_and_price_list', 'hidden', 1);
//        frm.refresh_field('currency_and_price_list');
//
//        frm.set_df_property('taxes_charges_section', 'hidden', 1);
//        frm.refresh_field('taxes_charges_section');
//
//        frm.set_df_property('taxes', 'hidden', 1);
//        frm.refresh_field('taxes');
//
//    }
//});
//
//frappe.ui.form.on('Purchase Receipt Item', {
//    form_render: function(frm, cdt, cdn) {
//        var row = locals[cdt][cdn];
//
//        frm.fields_dict['items'].grid.toggle_display('rate_and_amount', false);
//        frm.fields_dict['items'].grid.toggle_display('discount_and_margin_section', false);
//        frm.fields_dict['items'].grid.toggle_display('sec_break1', false);
//        frm.fields_dict['items'].grid.toggle_display('section_break_29', false);
//
//        frm.fields_dict['items'].grid.toggle_display('rate', false);
//        frm.fields_dict['items'].grid.toggle_display('amount', false);
//
//        frm.fields_dict['items'].grid.toggle_display('base_rate', false);
//        frm.fields_dict['items'].grid.toggle_display('base_amount', false);
//
//        frm.refresh_field('items');
//    }
//});
//
//
//
//frappe.ui.form.on('Purchase Receipt', {
//    onload: function(frm) {
//
//        frm.fields_dict['items'].grid.toggle_display('rate', false);
//        frm.fields_dict['items'].grid.toggle_display('amount', false);
//        frm.fields_dict['items'].grid.toggle_display('base_rate', false);
//        frm.fields_dict['items'].grid.toggle_display('base_amount', false);
//
//        frm.refresh_field('items');
//    }
//});





// **********************************
// **********************************


////Full payment is required to complete the invoice
//
//
//frappe.ui.form.on('POS Invoice', {
//	    validate: function(frm) {
//            if (frm.doc.is_pos) {
//                if (frm.doc.paid_amount < frm.doc.grand_total) {
//                    // frappe.throw(__('Full payment is required to complete the invoice.'));
//                    frappe.throw(__('يجب سداد المبلغ كاملا لاستكمال الفاتورة.'));
//                }
//                // if (frm.doc.paid_amount > frm.doc.grand_total) {
//                //     // frappe.throw(__('The paid amount exceeds the total. Please return the excess.'));
//                //     frappe.throw(__('المبلغ المدفوع يتجاوز المبلغ الإجمالي، يرجى إرجاع المبلغ الزائد.'));
//                // }
//            }
//    }
//});




// **********************************
// **********************************



////Search in the Item doctype for a record where the item_code matches the cost_center_number
//
//
//frappe.ui.form.on('Cost Center', {
//    cost_center_number: function(frm) {
//        if (frm.doc.cost_center_number) {
//            // Search in the Item doctype for a record where the item_code matches the cost_center_number
//            frappe.call({
//                method: 'frappe.client.get_list',
//                args: {
//                    doctype: 'Item',
//                    filters: {
//                        'item_code': frm.doc.cost_center_number  // Assuming the number matches with item_code
//                    },
//                    fields: ['item_code']
//                },
//                callback: function(r) {
//                    if (r.message && r.message.length > 0) {
//                        // Fetch the first matching item code
//                        let item_code = r.message[0].item_code;
//
//                        // Set the item_code_cost_center field with the fetched item code
//                        frm.set_value('item_code_cost_center', item_code);
//                    } else {
//                        // // If no item is found, clear the field or give a message
//                        // frappe.msgprint(__('No item found with this code.'));
//                        frm.set_value('item_code_cost_center', '');
//                    }
//                }
//            });
//        }
//    }
//});




// **********************************
// **********************************



////Fetch the corresponding cost center number from Cost Center doctype
//
//
//frappe.ui.form.on('Sales Invoice', {
//	refresh(frm) {
//		// your code here
//	}
//});
//
//
//frappe.ui.form.on('Sales Invoice', {
//    after_save(frm) {
//        // Loop through each item in the Sales Invoice
//        frm.doc.items.forEach(item => {
//            // Check if item_code is set
//            if (item.item_code) {
//                // Fetch the corresponding Cost Center name based on the item_code
//                frappe.db.get_value('Cost Center', {'item_code_cost_center': item.item_code}, 'name')
//                    .then(r => {
//                        // Set a default value for the cost center
//                        let default_cost_center_name = 'رئيسي - E';
//
//                        if (r.message && r.message.name) {
//                            let cost_center_name = r.message.name;
//
//                            // Set the cost_center field with the fetched Cost Center name
//                            frappe.model.set_value(item.doctype, item.name, 'cost_center', cost_center_name);
//
//                            frm.save();
//
//                            // // Optional: Show a message for confirmation
//                            // frappe.msgprint(__('Set Cost Center: ') + cost_center_name);
//                        } else {
//                            // // If no cost center is found, set the default value and show a message
//                            // frappe.msgprint(__('No cost center found for item: ') + item.item_code + '. Setting default cost center.');
//                            frappe.model.set_value(item.doctype, item.name, 'cost_center', default_cost_center_name);
//                        }
//                    })
//                    .catch(err => {
//                        frappe.msgprint(__('Error fetching Cost Center: ') + err);
//                    });
//            }
//        });
//
//        // Refresh the items table to reflect the changes
//        frm.refresh_field('items');
//    }
//});



// **********************************
// **********************************






// **********************************
// **********************************


// ====================== END Reference Code ====================================
// ==============================================================================







//// ==============================================================
//// ================== START Fetch Qty From Table Scrap Item in BOM ================


//frappe.ui.form.on('Stock Entry', {
//    validate: function(frm) {
//        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check_a_001 === 1 ) {
//            frappe.call({
//                method: "elfadaly_test_001.elfadaly_test_001.custom.fetch_qty_from_table_scrap_item_in_bom",
//                args: {
//                    doc: frm.doc.name
//                },
//                callback: function(r) {
//                    if (!r.exc) {
//                        frappe.show_alert({
//                            message: __('Fetch Qty From Table Scrap Item in BOM'),
//                            indicator: 'green'
//                        });
//////                        frm.reload_doc();
////                          frm.refresh_field('items');
//                    } else {
//                        frappe.msgprint(__('Error occurred while fetching data.'));
//                    }
//                }
//            });
//            frm.reload_doc();
//        }
//    }
//});



//// ================== END Fetch Qty From Table Scrap Item in BOM ================
//// ==============================================================






//// ==============================================================
//// ================== START Fetch Qty From Table Scrap Item in BOM -- No. 2 ================


frappe.ui.form.on('Stock Entry', {
    after_save: function(frm) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check_a_001 === 1 ) {
            frappe.call({
                method: "elfadaly_test_001.elfadaly_test_001.custom.fetch_qty_from_table_scrap_item_in_bom_no_2",
                args: {
                    doc: frm.doc.name
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.show_alert({
                            message: __('Fetch Qty From Table Scrap Item in BOM'),
                            indicator: 'green'
                        });
////                        frm.reload_doc();
//                          frm.refresh_field('items');
                    } else {
                        frappe.msgprint(__('Error occurred while fetching data.'));
                    }
                }
            });
            frm.reload_doc();
        }
    }
});



//// ================== END Fetch Qty From Table Scrap Item in BOM  -- No. 2 ================
//// ==============================================================













// ==============================================================================
// ==============================================================================
// ========= START Updated bom_check_a_001 field to Checked (1) ==============



frappe.ui.form.on('Stock Entry', {
    after_save: function (frm) {
        if (frm.doc.stock_entry_type === 'Manufacture') {
            frappe.call({
                method: "elfadaly_test_001.elfadaly_test_001.custom.fetch_bom_check_a_001",
                args: {
                    doc: frm.doc.name
                },
                callback: function (r) {
                    if (!r.exc) {
                        frappe.show_alert({
                            message: __('Updated bom_check_a_001 field to Checked (1)'),
                            indicator: 'green'
                        });
                    } else {
                        frappe.msgprint(__('Error occurred while updating bom_check_a_001.'));
                    }
                }
            });
            frm.reload_doc();
        }
    }
});




// ========= END Updated bom_check_a_001 field to Checked (1) ==============
// ==============================================================================
// ==============================================================================







// ==============================================================================
// ==============================================================================
// ==============================================================================





