# test_mathops.py
import unittest
from mathops import add, subtract, multiply, divide

class TestMathOps(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 7), 28)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
