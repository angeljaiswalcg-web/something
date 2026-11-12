
import unittest

from tools.calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(
            calculate(10, 5, "addition"),
            (15, "+")
        )

    def test_uppercase_operation(self):
        self.assertEqual(
            calculate(10, 5, "ADDITION"),
            (15, "+")
        )

    def test_zero_divided_by_eight(self):
        self.assertEqual(
            calculate(0, 8, "division"),
            (0, "÷")
        )

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(8, 0, "division")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(10, 5, "power")


if __name__ == "__main__":
    unittest.main()
