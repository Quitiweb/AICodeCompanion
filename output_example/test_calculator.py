import unittest
from output_example.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        result = self.calc.calculate(5, 4, 'SUM')
        self.assertEqual(result, 9)

    def test_res(self):
        result = self.calc.calculate(5, 4, 'RES')
        self.assertEqual(result, 1)

    def test_mul(self):
        result = self.calc.calculate(5, 4, 'MUL')
        self.assertEqual(result, 20)

    def test_div(self):
        result = self.calc.calculate(20, 4, 'DIV')
        self.assertEqual(result, 5)
    
    def test_div_by_zero(self):
        result = self.calc.calculate(9, 0, 'DIV')
        self.assertEqual(result, 'You cannot divide by 0')

    def test_invalid_operation(self):
        result = self.calc.calculate(5, 4, 'EXP')
        self.assertEqual(result, 'Invalid operation')

    def test_non_numeric_input(self):
        result = self.calc.calculate('a', 4, 'SUM')
        self.assertEqual(result, 'Invalid input: numbers must be int or float')

    def test_non_numeric_input_for_second_parameter(self):
        result = self.calc.calculate(4, 'b', 'SUM')
        self.assertEqual(result, 'Invalid input: numbers must be int or float')

    def test_upper_bound_numeric_input_handling(self):
        result = self.calc.calculate(1e309, 1e309, 'SUM')
        self.assertTrue(result)  # Should not fail, handle gracefully

    def test_valid_float_input(self):
        result = self.calc.calculate(1.5, 2.5, 'SUM')
        self.assertEqual(result, 4.0)

if __name__ == '__main__':
    unittest.main()
