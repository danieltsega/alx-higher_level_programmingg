#!/usr/bin/python3
"""A Rectangle test Module"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestingSquare(unittest.TestCase):
    """A class that tests a square
    class
    """

    def setUp(self):
        """A function that is called
        in every test functions
        """

        Base._Base__nb_objects = 0

    def test_private_attribute(self):
        """A method that tests the access
        of the width attribute
        """

        S = Square(1, 2)
        with self.assertRaises(AttributeError):
            S.__width

    def test_private_attribute_2(self):
        """A method that tests the access
        of the height attribute
        """

        S = Square(1, 2)
        with self.assertRaises(AttributeError):
            S.__height

    def test_private_attribute_3(self):
        """A method that tests the access
        of the x attribute
        """

        S = Square(1, 2)
        with self.assertRaises(AttributeError):
            S.__x

    def test_private_attribute_4(self):
        """A method that tests the access
        of the y attribute
        """

        S = Square(1, 2)
        with self.assertRaises(AttributeError):
            S.__y

    def test_all_attributes_given(self):
        """A method that tests if all
        attributes are given
        """

        S = Square(2, 3, 4, 2)
        self.assertEqual(S.size, 2)
        self.assertEqual(S.width, 2)
        self.assertEqual(S.height, 2)
        self.assertEqual(S.x, 3)
        self.assertEqual(S.y, 4)
        self.assertEqual(S.id, 2)

    def test_xyid_default_value(self):
        """A method that tests for the
        default value of id, x and y
        """

        S = Square(5, 6)
        self.assertEqual(S.size, 5)
        self.assertEqual(S.width, 5)
        self.assertEqual(S.height, 5)
        self.assertEqual(S.x, 6)
        self.assertEqual(S.y, 0)
        self.assertEqual(S.id, 1)

    def test_invalid_value(self):
        """A method that tests if
        we give a string value to
        width
        """

        with self.assertRaises(TypeError):
            S = Square("3", 4)

    def test_invalid_value_2(self):
        """A method that tests if
        we give a string value t
        height
        """

        with self.assertRaises(TypeError):
            S = Square(4, "5")

    def test_invalid_value_3(self):
        """A method that tests if
        we give it a string value to
        x
        """

        with self.assertRaises(TypeError):
            S = Square(4, 5, "3")

    def test_invalid_value_4(self):
        """A method that tests if
        we give a string value to
        y
        """

        with self.assertRaises(TypeError):
            S = Square(4, 5, "3", 4)
