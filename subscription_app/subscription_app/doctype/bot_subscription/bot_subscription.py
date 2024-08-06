# Copyright (c) 2024, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import today, add_to_date, date_diff


class BotSubscription(Document):
	pass	
		

def auto_renewal_subscription():
	bot_subscriptions = frappe.get_all('Bot Subscription', fields=['customer', 'end_date', 'start_date', 'auto_renew', 'name'], filters={'auto_renew': 1})

	for bot_subscription in bot_subscriptions:
		difference_of_date = date_diff(bot_subscription.end_date, today())
		
		if (difference_of_date == 0):
			day_difference = date_diff(bot_subscription.end_date, bot_subscription.start_date)
			
			new_start_date = add_to_date(bot_subscription.start_date, days=(day_difference + 1))
			new_end_date = add_to_date(bot_subscription.end_date, days=(day_difference + 1))

			new_doc = frappe.get_doc('Bot Subscription', bot_subscription.name)

			new_doc.start_date = new_start_date
			new_doc.end_date = new_end_date

			new_doc.insert()
			frappe.db.commit()
				

def send_reminder_email_to_customer():
	bot_subscriptions = frappe.get_all('Bot Subscription', fields=['customer', 'email_template', 'end_date', 'remind_before_days', 'send_reminder'], filters={'send_reminder': 1})

	for bot_subscription in bot_subscriptions:
		days_to_reminder = -int(bot_subscription.remind_before_days)
		reminder_date = add_to_date(bot_subscription.end_date, days=days_to_reminder)
		difference_of_date = date_diff(reminder_date, today())
	
		if (difference_of_date == 0):
			customer_emails = get_customer_emails(customer=bot_subscription.customer)

			if (customer_emails):
				parent_doc = frappe.get_doc('Bot Subscription', bot_subscription)
				email_template = frappe.get_doc('Email Template', bot_subscription.email_template)
				subject = frappe.render_template(email_template.subject, parent_doc.as_dict())
				message = frappe.render_template(email_template.response, parent_doc.as_dict())
				
				frappe.sendmail(subject=subject, recipients=customer_emails, message = message)


def send_reminder_email_to_admin():
	bot_subscriptions = frappe.get_all('Bot Subscription', fields=['customer', 'email_template', 'end_date', 'remind_before_days', 'send_email_to_admin'], filters={'send_email_to_admin': 1})

	super_admin = frappe.get_doc('User', 'Administrator')
	super_admin_email = super_admin.email

	for bot_subscription in bot_subscriptions:
		days_to_reminder = -int(bot_subscription.remind_before_days)
		reminder_date = add_to_date(bot_subscription.end_date, days=days_to_reminder)
		difference_of_date = date_diff(reminder_date, today())
	
		if (difference_of_date == 0):

			parent_doc = frappe.get_doc('Bot Subscription', bot_subscription)
			email_template = frappe.get_doc('Email Template', bot_subscription.email_template)
			subject = frappe.render_template(email_template.subject, parent_doc.as_dict())
			message = frappe.render_template(email_template.response, parent_doc.as_dict())

			if (super_admin_email and super_admin_email is not None):
				frappe.sendmail( subject=subject, recipients = [super_admin_email], message = message)


def get_customer_emails(customer):
	contact_links = frappe.get_all('Dynamic Link', filters={
		'parenttype': 'Contact',
		'link_doctype': 'Customer',
        'link_name': customer
    }, fields=['parent'])
	
	emails = []
	
	for link in contact_links:
		contact_emails = frappe.get_all('Contact Email', filters={'parent': link.parent}, fields=['email_id'])
		for email in contact_emails:
			if email.email_id:
				emails.append(email.email_id)
	
	return emails if emails else None	