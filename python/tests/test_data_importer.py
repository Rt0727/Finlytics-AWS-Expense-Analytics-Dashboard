import unittest
from data_importer import DataImporter

class TestDataImporter(unittest.TestCase):
    def setUp(self):
        self.data_importer = DataImporter()

    def test_import_valid_csv(self):
        result = self.data_importer.import_csv("valid_data.csv")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_import_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            self.data_importer.import_csv("nonexistent_file.csv")

    def test_import_empty_csv(self):
        result = self.data_importer.import_csv("empty_data.csv")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()