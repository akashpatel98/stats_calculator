import unittest

from Calculator.calculator import Calculator
from Calculator import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertIsInstance(self.calculator.result, 0)

    def test_subtraction(self):
        test_data = CsvReader('/tests/CSV_files/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data = CsvReader('/CSV_files/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main':
    unittest.main()
