#!/usr/bin/python3
"""A Rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """A rectangle class that
    inherits a base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constractor method"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """A width getter method"""

        return self.__width

    @width.setter
    def width(self, width):
        """A with setter method"""

        self.__width = width

    @property
    def height(self):
        """A height getter method"""

        return self.__height

    @height.setter
    def height(self, height):
        """A height setter method"""

        self.__height = height

    @property
    def x(self):
        """A x getter method"""

        return self.__x

    @x.setter
    def x(self, x):
        """A x setter method"""

        self.__x = x

    @property
    def y(self):
        """A y getter method"""

        return self.__y

    @y.setter
    def y(self, y):
        """A y setter method"""

        self.__y = y
