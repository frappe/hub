# Copyright (c) 2015, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

import frappe, json

@frappe.whitelist(allow_guest=True)
def register(seller_name, seller_email, seller_country, seller_website=None, seller_city=None,
		seller_description=None):
	"""Register on the hub."""
	seller = frappe.new_doc("Hub Seller")
	for key in ("seller_name", "seller_website", "seller_city", "seller_email",
	"seller_country", "seller_description"):
		seller.set(key, locals()[key])
	seller.insert(ignore_permissions=True)
	return seller.as_dict()

@frappe.whitelist(allow_guest=True)
def sync(access_token, items, item_list):
	"""Sync new items"""
	seller = get_seller(access_token)
	# delete if not in item list
	all_items = frappe.db.sql_list("select item_code from `tabHub Item` where hub_seller=%s", seller.name)
	item_list = json.loads(item_list)
	for item in all_items:
		if item not in item_list:
			frappe.delete_doc("Hub Item", item)

	# insert / update items
	for item in json.loads(items):
		item_name = frappe.db.get_value("Hub Item",
			{"hub_seller": seller.name, "item_code": item.get("name")})
		if item_name:
			hub_item = frappe.get_doc("Hub Item", item_name)
		else:
			hub_item = frappe.new_doc("Hub Item")
			hub_item.hub_seller = seller.name

		for key in ("item_code", "item_name", "description", "image", "item_group"):
			hub_item.set(key, item.get(key))

		for key in ("seller_name", "seller_email", "seller_country", "seller_city"):
			hub_item.set(key, seller.get(key))

		hub_item.published = 1
		hub_item.save(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def get_items(access_token, text, country=None, start=0, limit=50):
	"""Returns list of items by filters"""
	get_seller(access_token)
	or_filters = [
		{"item_name": ["like", "%{0}%".format(text)]},
		{"description": ["like", "%{0}%".format(text)]}
	]
	filters = {
		"published": 1
	}
	if country:
		filters["country"] = country
	return frappe.get_all("Hub Item", fields=["item_code", "item_name", "description", "image",
		"seller_name", "seller_email", "seller_country", "seller_city"],
			filters=filters, or_filters=or_filters, limit_start = start, limit_page_length = limit)

@frappe.whitelist(allow_guest=True)
def delete(access_token, item_code):
	"""Delete item on portal"""
	seller = get_seller(access_token)
	item = frappe.db.get_value("Hub Item", {"item_code": item_code, "hub_seller": seller.name})
	if item:
		frappe.delete_doc("Hub Item", item)

@frappe.whitelist(allow_guest=True)
def update_seller(access_token, args):
	"""Update seller details"""
	seller = get_seller(access_token)
	for key, val in json.loads(args).iteritems():
		seller.set(key, val)
	seller.save(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def unpublish(access_token):
	"""Un publish seller"""
	seller = get_seller(access_token)
	seller.published=0
	seller.save(ignore_permissions=True)

def get_seller(access_token):
	return frappe.get_doc("Hub Seller", {"access_token": access_token})

