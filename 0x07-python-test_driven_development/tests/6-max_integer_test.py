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

    def test_max_end(self):
        self.assertEqual(max_integer([1,2,3,4,5]), 5)

    def test_max_start(self):
        self.assertEqual(max_integer([5,3,4,2,1]), 5)

    """Tests for Problematic conditions"""

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([5, (3, 4)])

    def test_integer(self):
        with self.assertRaises(TypeError):
            max_integer(4)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([5, 'Danny'])
