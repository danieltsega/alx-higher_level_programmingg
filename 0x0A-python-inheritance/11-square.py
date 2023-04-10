#!/usr/bin/python3
"""A Square Module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        """An init method"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """A methid that gets area from
        the parent class
        """

        return super().area()

    def __str__(self):
        """A method that return a description
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
