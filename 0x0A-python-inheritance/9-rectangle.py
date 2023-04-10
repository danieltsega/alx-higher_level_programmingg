#!/usr/bin/python3
"""A Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangele
    """

    def __init__(self, width, height):
        """An instantinous method
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A method that returns
        the area of the class
        """

        return (self.__width * self.__height)

    def __str__(self):
        """A method that prints a
        Description
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
