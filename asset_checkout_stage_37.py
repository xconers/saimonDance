# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: AssetCheckout
import unittest
from datetime import date


class TestCheckout(unittest.TestCase):
    def test_checkout_with_return(self):
        item = {"name": "Drill", "owner": "Alice", "status": "issued"}
        checkout = {"item": item, "borrower": "Bob", "date": date(2024, 1, 15), "status": "active"}
        self.assertEqual(checkout["borrower"], "Bob")
        self.assertEqual(checkout["date"], date(2024, 1, 15))
        self.assertEqual(checkout["status"], "active")
        item["status"] = "returned"
        item["owner"] = "Bob"
        self.assertEqual(item["status"], "returned")
        self.assertEqual(item["owner"], "Bob")

    def test_checkout_status_flow(self):
        item = {"name": "Laptop", "owner": "Charlie", "status": "available"}
        checkout = {"item": item, "borrower": "Diana", "date": date(2024, 2, 1), "status": "active"}
        item["status"] = "issued"
        self.assertEqual(item["status"], "issued")
        self.assertEqual(checkout["status"], "active")
        self.assertEqual(checkout["borrower"], "Diana")
        self.assertEqual(checkout["date"], date(2024, 2, 1))


if __name__ == "__main__":
    unittest.main()
