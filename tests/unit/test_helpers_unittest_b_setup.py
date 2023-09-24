import unittest
from app.utilities.complicated_helpers import Calculator


class TestCalculatorWithSetup(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_second(self):
        self.assertEqual(self.calc.add(0, 5), 5)


if __name__ == "__main__":
    unittest.main()
