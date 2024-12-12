import unittest
from dashboard_manager import DashboardManager

class TestDashboardManager(unittest.TestCase):
    def setUp(self):
        self.dashboard_manager = DashboardManager()

    def test_generate_summary(self):
        data = [
            {"category": "Food", "amount": 100},
            {"category": "Transport", "amount": 50}
        ]
        summary = self.dashboard_manager.generate_summary(data)
        self.assertIn("total_expenses", summary)
        self.assertEqual(summary["total_expenses"], 150)

    def test_generate_empty_summary(self):
        data = []
        summary = self.dashboard_manager.generate_summary(data)
        self.assertEqual(summary["total_expenses"], 0)

    def test_visualize_data(self):
        data = [
            {"category": "Food", "amount": 100},
            {"category": "Transport", "amount": 50}
        ]
        result = self.dashboard_manager.visualize_data(data)
        self.assertTrue(result)  # Assuming the method returns True on success

if __name__ == "__main__":
    unittest.main()