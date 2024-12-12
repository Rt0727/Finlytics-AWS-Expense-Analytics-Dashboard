import unittest
from expense_calculator import ExpenseCalculator

class TestExpenseCalculator(unittest.TestCase):
    def setUp(self):
        self.expense_calculator = ExpenseCalculator()

    def test_calculate_total_expenses(self):
        data = [
            {"category": "Food", "amount": 100},
            {"category": "Transport", "amount": 50}
        ]
        total = self.expense_calculator.calculate_total(data)
        self.assertEqual(total, 150)

    def test_calculate_category_expenses(self):
        data = [
            {"category": "Food", "amount": 100},
            {"category": "Transport", "amount": 50},
            {"category": "Food", "amount": 30}
        ]
        food_total = self.expense_calculator.calculate_by_category(data, "Food")
        self.assertEqual(food_total, 130)

    def test_calculate_empty_data(self):
        data = []
        total = self.expense_calculator.calculate_total(data)
        self.assertEqual(total, 0)

if __name__ == "__main__":
    unittest.main()