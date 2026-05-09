import unittest
from datetime import datetime, timedelta
from app import find_expiring_products


class TestFindExpiringProducts(unittest.TestCase):

    def test_basic_case(self):
        today = datetime.today()

        products = [
            {
                "name": "Молоко",
                "expiry": (today + timedelta(days=3)).strftime("%Y-%m-%d")
            },
            {
                "name": "Сир",
                "expiry": (today + timedelta(days=10)).strftime("%Y-%m-%d")
            },
            {
                "name": "Хліб",
                "expiry": (today + timedelta(days=1)).strftime("%Y-%m-%d")
            }
        ]

        expected = ["Молоко", "Хліб"]

        self.assertEqual(
            sorted(find_expiring_products(products)),
            sorted(expected)
        )

    def test_empty_list(self):
        products = []

        expected = []

        self.assertEqual(find_expiring_products(products), expected)

    def test_all_products_far_expiry(self):
        today = datetime.today()

        products = [
            {
                "name": "Сік",
                "expiry": (today + timedelta(days=20)).strftime("%Y-%m-%d")
            }
        ]

        expected = []

        self.assertEqual(find_expiring_products(products), expected)

    def test_all_products_expiring(self):
        today = datetime.today()

        products = [
            {
                "name": "Йогурт",
                "expiry": (today + timedelta(days=2)).strftime("%Y-%m-%d")
            },
            {
                "name": "Кефір",
                "expiry": (today + timedelta(days=5)).strftime("%Y-%m-%d")
            }
        ]

        expected = ["Йогурт", "Кефір"]

        self.assertEqual(
            sorted(find_expiring_products(products)),
            sorted(expected)
        )


if __name__ == "__main__":
    unittest.main()
