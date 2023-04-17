#!/usr/bin/python3
"""A Test Base Module"""


import unittest
from models.base import Base


class TestingBase(unittest.TestCase):
    """A class that is used to test
    the Base class
    """

    def setUp(self):
        """A method that is called
        in every test
        """

        Base._Base__nb_objects = 0

    def test_default_id(self):
        """A method to test the default
        id of the base class"""

        B = Base()
        self.assertEqual(B.id, 1)

    def test_id(self):
        """A method to test a given id
        """

        B = Base(1)
        self.assertEqual(B.id, 1)

    def test_id_increament(self):
        """A method to test the __nb_objects
        on the id attribute
        """

        B = Base()
        B2 = Base()
        B3 = Base()
        B4 = Base()
        self.assertEqual(B.id, 1)
        self.assertEqual(B2.id, 2)
        self.assertEqual(B3.id, 3)
        self.assertEqual(B4.id, 4)

    def test_with_more_args(self):
        """A method that tests by giving morethan
        one args as id to Base
        """

        with self.assertRaises(TypeError):
            B = Base(2, 4, 5)

    def test_string_id(self):
        """A method to test by giving
        a string value to id
        """

        B = Base("2")
        self.assertEqual(B.id, "2")

    def test_duplicate_id(self):
        """A method that test a given
        dupilicate id value
        """

        B = Base(3)
        B2 = Base(2)
        B3 = Base()
        self.assertEqual(B.id, 3)
        self.assertEqual(B2.id, 2)
        self.assertEqual(B3.id, 1)

    def test_access_private_attribute(self):
        """A method that tests the access
        of a private class attribute
        """

        B = Base()
        with self.assertRaises(AttributeError):
            B.__nb_objects
