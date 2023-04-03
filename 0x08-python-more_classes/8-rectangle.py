#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Creates a class of a rectangle object
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """A method to initialise the object
        Args:
            width - the width of the rectangel
            height - the height of the rectangel
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """A width getter function
        Return: the width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """A width setter function
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A height getter function
        Return: the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A height setter function
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that returns the area of
        the rectangle object
        Return: the area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """A function that returns the perimeter
        of the rectangle object
        Return: the perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """A function that returns the rectangle
        as #
        Return: the rectangle as #
        """

        rect = ""
        if self.width == 0 or self.height == 0:
            return rect

        for i in range(self.height):
            rect += (str(self.print_symbol) * self.width) + "\n"

        return rect[0:-1]

    def __repr__(self):
        """A function that returns the string
        representation of  an object
        Return: string representation of
                the rectangle
        """

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """A function that returns a string
        when the object is deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A static method that compares
        two rectangles and return the biggest
        if not equal
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() == rect_2.area():
            return rect_1
