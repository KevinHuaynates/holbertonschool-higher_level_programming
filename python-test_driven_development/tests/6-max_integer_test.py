#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_max_integer_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_integer_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 1.4]), 3.5)

    def test_max_integer_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3, 4])

if __name__ == '__main__':
    unittest.main()
