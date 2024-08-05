// Copyright (c) 2024, khayam khan and contributors
// For license information, please see license.txt


frappe.ui.form.on('Bot Subscription', {
	refresh(frm) {
		calculate_total_days(frm);
	},

    start_date: function(frm) {
        calculate_total_days(frm);
    },

    end_date: function(frm) {
        calculate_total_days(frm);
    }
})


function calculate_total_days(frm) {
    if (frm.doc.start_date && frm.doc.end_date) {

        var start_date = moment(frm.doc.start_date);
        var end_date = moment(frm.doc.end_date);

        var total_days = end_date.diff(start_date, 'days');

        frm.set_value('total_days', total_days);
    } else {
        frm.set_value('total_days', null);
    }
}