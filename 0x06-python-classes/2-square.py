#!/usr/bin/python3
"""Defining a square Class"""


class Square:
    """A Class that defines a Square
    """

    def __init__(self, size=0):
        """A method that defines a private instance
        variable

        Args:
            size: The size of the square object.

        Raises:
            TypeError: Is raised if size isn't int.
            ValueError: Is raised if size is negative.
        """

        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
