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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A width getter method"""

        return self.__width

    @width.setter
    def width(self, width):
        """A with setter method"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """A height getter method"""

        return self.__height

    @height.setter
    def height(self, height):
        """A height setter method"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """A x getter method"""

        return self.__x

    @x.setter
    def x(self, x):
        """A x setter method"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """A y getter method"""

        return self.__y

    @y.setter
    def y(self, y):
        """A y setter method"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """An Area calculating method"""

        return self.__width * self.__height

    def display(self):
        """A method to display rectangle"""

        rect = self.y * "\n"
        for i in range(self.height):
            rect += (" " * self.x)
            rect += ("#" * self.width) + "\n"

        print(rect, end="")

    def __str__(self):
        """A str method"""

        str_cls = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} ".format(self.x, self.y)
        str_wihe = "{}/{}".format(self.width, self.height)

        return str_cls + str_id + str_xy + str_wihe
