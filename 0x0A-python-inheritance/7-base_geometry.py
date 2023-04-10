#!/usr/bin/python3
"""A BaseGeometry Module
"""


class BaseGeometry:
    """A Base Geometry class
    """

    def area(self):
        """A public method that raises
        some exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public method that validates
        the value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
