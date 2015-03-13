import frappe, unittest, json
import hub.api

class TestHub(unittest.TestCase):
	def setUp(self):
		self.seller = hub.api.register("Frappe", "info@erpnext.com", "India", seller_website="https://erpnext.com")

		self.assertTrue(self.seller.get("name"))
		self.assertTrue(self.seller.get("access_token"))

	def test_sync(self):
		items = [
			{"item_code": "SUP", "item_name": "Startup Hosting",
				"description": "ERPNext Cloud Hosting for 2 users."},
			{"item_code": "SMB", "item_name": "Small Business Hosting",
				"description": "ERPNext Cloud Hosting for 5 users."},
			{"item_code": "ENT", "item_name": "Enterprise Hosting",
				"description": "ERPNext Cloud Hosting for 10 users."},
		]

		hub.api.sync(self.seller.access_token, items = json.dumps(items))

		result = hub.api.get_items(self.seller.access_token, "erpnext")

		for i in range(3):
			self.assertTrue(items[i].get("item_code") in [r["item_code"] for r in result])

		for item in items:
			hub.api.delete(self.seller.access_token, item.get("item_code"))

	def tearDown(self):
		frappe.delete_doc("Hub Seller", self.seller.get("name"))
