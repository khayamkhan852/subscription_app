# Copyright (c) 2024, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import today, add_to_date, date_diff


class BotSubscription(Document):
	pass



def send_reminder_emails():
	bot_subscriptions = frappe.get_all('Bot Subscription', fields=['customer', 'email_template', 'end_date', 'remind_before_days', 'send_reminder', 'send_email_to_admin'])
	
	super_admin = frappe.get_doc('User', 'Administrator')
	super_admin_email = super_admin.email

	for bot_subscription in bot_subscriptions:
		days_to_reminder = -int(bot_subscription.remind_before_days)
		reminder_date = add_to_date(bot_subscription.end_date, days=days_to_reminder)
		difference_of_date = date_diff(reminder_date, today())
	
		if (difference_of_date == 0):
			customer_email = get_customer_email(customer=bot_subscription.customer)

			parent_doc = frappe.get_doc('Bot Subscription', bot_subscription)
			email_template = frappe.get_doc('Email Template', bot_subscription.email_template)
			subject = frappe.render_template(email_template.subject, parent_doc.as_dict())
			message = frappe.render_template(email_template.response, parent_doc.as_dict())

			if (bot_subscription.send_reminder and bot_subscription.send_reminder is not 0 and customer_email is not None):
				frappe.sendmail( subject=subject, recipients = [customer_email], message = message)
		
			if (bot_subscription.send_email_to_admin and bot_subscription.send_email_to_admin is not 0 and super_admin_email and super_admin_email is not None):
				frappe.sendmail( subject=subject, recipients = [super_admin_email], message = message)


def get_customer_email(customer):
	address_links = frappe.get_all('Dynamic Link', filters={
		'parenttype': 'Address',
		'link_doctype': 'Customer',
		'link_name': customer
	}, fields=['parent'])
	
	for link in address_links:
		email = frappe.get_value('Address', link.parent, 'email_id')
		if email:
			return email			
	return None