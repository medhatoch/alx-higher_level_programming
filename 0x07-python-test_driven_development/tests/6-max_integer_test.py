#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from parameterized import parameterized
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    @parameterized.expand([
        ([1, 3, 4, 2], 4),
        ([10, 10, 10], 10),
        ([0, 0, 0, 0], 0),
        ([-1, -2, -3, -4], -1),
    ])
    def test_parameterized_cases(self, input_list, expected_output):
        self.assertEqual(max_integer(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()
