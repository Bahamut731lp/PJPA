import unittest
from triangle import *

class TestStringMethods(unittest.TestCase):
    def test_negative_side(self):
        actual = triangle(5, -1, 5)
        expected = False
        self.assertEqual(actual, expected)

    def test_negative_sides(self):
        actual = triangle(-3.9, -1.58, -1.22)
        expected = False
        self.assertEqual(actual, expected)

    def test_zero_sides(self):
        actual = triangle(0, 0, 0)
        expected = False
        self.assertEqual(actual, expected)

    def test_proper_triangle(self):
        actual = triangle(10, 8, 9)
        expected = False
        self.assertEqual(actual, expected)

    def test_rightangle_triangle(self):
        actual = triangle(3, 4, 5)
        expected = True
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()