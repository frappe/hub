# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import random_string

class HubSeller(Document):
	def autoname(self):
		self.name = random_string(16)
		self.access_token = random_string(16)

	def validate(self):
		if not self.is_new():
			published = frappe.db.get_value(self.doctype, self.name, "published")
		if published and not self.published:
			frappe.db.sql("update `tabHub Item` set published=0 where hub_seller=%s", self.name)
		if not published and self.published:
			frappe.db.sql("update `tabHub Item` set published=1 where hub_seller=%s", self.name)

