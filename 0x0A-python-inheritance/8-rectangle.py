#!/usr/bin/python
"""The Rectangle Module
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangele
    """

    def __init__(self, width, height):
        """An instantinous method
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
