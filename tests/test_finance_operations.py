import unittest
from unittest.mock import patch  # Добавлен им

import pandas as pd

# порт patch
from src.finance_operations import read_csv_transactions, read_excel_transactions


class TestFinanceOperations(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_read_csv_transactions(self, mock_read_csv):
        # Мокируем возвращаемое значение pd.read_csv
        mock_read_csv.return_value = pd.DataFrame([{"date": "2023-01-01", "amount": 100}])

        # Вызываем тестируемую функцию
        result = read_csv_transactions("dummy_path.csv")

        # Проверяем, что результат соответствует ожидаемому
        self.assertEqual(result, [{"date": "2023-01-01", "amount": 100}])

    @patch("pandas.read_excel")
    def test_read_excel_transactions(self, mock_read_excel):
        # Мокируем возвращаемое значение pd.read_excel
        mock_read_excel.return_value = pd.DataFrame([{"date": "2023-01-01", "amount": 200}])

        # Вызываем тестируемую функцию
        result = read_excel_transactions("dummy_path.xlsx")

        # Проверяем, что результат соответствует ожидаемому
        self.assertEqual(result, [{"date": "2023-01-01", "amount": 200}])


if __name__ == "__main__":
    unittest.main()
