#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for Normal cases"""

    def test_normal(self):
        self.assertEqual(max_integer([10, 20, 50, 40]), 50)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([19]), 19)

    def test_negative(self):
        self.assertEqual(max_integer([-38, -44, -12, -57]), -12)

