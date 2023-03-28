#!/usr/bin/python3
"""Defining a Square Class"""


class Square:
    """A Class that defines a square
    """

    def __init__(self, size=0):
        """A method that accepts arguments
        and initialaizes them.

        Args:
            size: A size of the square object.

        Raises:
            TypeError: Due to size not being int.
            ValueError: Due to size being negative.
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """A method that returns the area
        of a square.

        Args:
            None: only self argument is passed.
        """
        return self.__size ** 2
