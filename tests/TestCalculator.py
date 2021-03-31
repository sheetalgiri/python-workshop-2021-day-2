import unittest
from projects.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This is called immediately before calling the test method; more info https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.calc = Calculator()

    def test_add(self):
        value = self.calc.add(2.0, 3.0)
        self.assertEqual(value, 5.0, "Incorrect Answer")
        self.assertEqual(value, self.calc.last_answer, "Incorrect Answer")

    def test_subtract(self):
        value = self.calc.subtract(3.0, 2.0)
        self.assertEqual(value, 1.0, "Incorrect Answer")
        self.assertEqual(value, self.calc.last_answer, "Incorrect Answer")

if __name__ == '__main__':
    unittest.main()

#run with python -m unittest tests.TestCalculator