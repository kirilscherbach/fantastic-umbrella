import unittest
from app.utilities.helpers import add


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    # assertCountEqual
    # assertListEqual
    # assertTrue
    # assertRaises

    # def test_badd(self):
    #    """this test will fail"""
    #    self.assertEqual(add(2, 2), 5)


if __name__ == "__main__":
    unittest.main()
