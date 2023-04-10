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
