#!/usr/bin/python3
"""A Rectangle test Module"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestingRectangle(unittest.TestCase):
    """A class that tests a rectangle
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

        R = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            R.__width

    def test_private_attribute_2(self):
        """A method that tests the access
        of the height attribute
        """

        R = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            R.__height

    def test_private_attribute_3(self):
        """A method that tests the access
        of the x attribute
        """

        R = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            R.__x

    def test_private_attribute_4(self):
        """A method that tests the access
        of the y attribute
        """

        R = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            R.__y

    def test_all_attributes_given(self):
        """A method that tests if all
        attributes are given
        """

        R = Rectangle(2, 3, 3, 4, 2)
        self.assertEqual(R.width, 2)
        self.assertEqual(R.height, 3)
        self.assertEqual(R.x, 3)
        self.assertEqual(R.y, 4)
        self.assertEqual(R.id, 2)

    def test_xyid_default_value(self):
        """A method that tests for the
        default value of id, x and y
        """

        R = Rectangle(5, 6)
        self.assertEqual(R.width, 5)
        self.assertEqual(R.height, 6)
        self.assertEqual(R.x, 0)
        self.assertEqual(R.y, 0)
        self.assertEqual(R.id, 1)

    def test_invalid_value(self):
        """A method that tests if
        we give a string value to
        width
        """

        with self.assertRaises(TypeError):
            R = Rectangle("3", 4)

    def test_invalid_value_2(self):
        """A method that tests if
        we give a string value t
        height
        """

        with self.assertRaises(TypeError):
            R = Rectangle(4, "5")

    def test_invalid_value_3(self):
        """A method that tests if
        we give it a string value to
        x
        """

        with self.assertRaises(TypeError):
            R = Rectangle(4, 5, "3")

    def test_invalid_value_4(self):
        """A method that tests if
        we give a string value to
        y
        """

        with self.assertRaises(TypeError):
            R = Rectangle(4, 5, 3, "4")

    def test_area(self):
        """A method to test area
        """

        R = Rectangle(5, 4)
        self.assertEqual(R.area(), 20)

    def test_create_method(self):
        """A method to test the create
        method of the rectangle class
        """

        dic = {'id': 4, 'width': 5, 'height': 3, 'x': 2, 'y': 1}
        R = Rectangle.create(**dic)
        self.assertEqual(R.id, 4)
        self.assertEqual(R.width, 5)
        self.assertEqual(R.height, 3)
        self.assertEqual(R.x, 2)
        self.assertEqual(R.y, 1)

    def test_load(self):
        """A method to test a load
        file method
        """

        load = Rectangle.load_from_file()
        self.assertEqual(load, load)
