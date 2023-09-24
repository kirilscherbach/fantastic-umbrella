import unittest


class TestIntrospection(unittest.TestCase):
    def test_eq_long_text(self):
        a = "1" * 100 + "a" + "2" * 100
        b = "1" * 100 + "b" + "2" * 100
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
