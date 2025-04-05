#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_cases(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-1]), -1)

    def test_multiple_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3])

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_none_as_input(self):
        self.assertIsNone(max_integer(None))

if __name__ == '__main__':
    unittest.main()
