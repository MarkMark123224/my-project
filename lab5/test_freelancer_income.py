import unittest
from freelancer_income import (calculate_hours_payment, subtract_platform_fee,
                               analyze_income)


class TestFreelancerIncome(unittest.TestCase):

    def test_hours_payment_normal(self):
        self.assertEqual(calculate_hours_payment(10, 5), 50)

    def test_hours_payment_zero(self):
        self.assertEqual(calculate_hours_payment(0, 10), 0)

    def test_hours_payment_negative(self):
        with self.assertRaises(ValueError):
            calculate_hours_payment(-1, 5)

    def test_fee_normal(self):
        self.assertEqual(subtract_platform_fee(100, 10), 90.0)

    def test_fee_zero(self):
        self.assertEqual(subtract_platform_fee(100, 0), 100.0)

    def test_fee_full(self):
        self.assertEqual(subtract_platform_fee(100, 100), 0.0)

    def test_fee_invalid(self):
        with self.assertRaises(ValueError):
            subtract_platform_fee(100, -5)

    def test_analyze_income(self):
        expected = {
            "gross_income": 50,
            "net_income": 45.0
        }
        self.assertEqual(analyze_income(10, 5, 10), expected)


if __name__ == "__main__":
    unittest.main()
