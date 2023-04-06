#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing max_integer function."""
    def test_max(self):
        """Tests the correct output of the functoin."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_empty(self):
        """Tests if the list of integers is empty."""
        self.assertIs(max_integer([]), None)
