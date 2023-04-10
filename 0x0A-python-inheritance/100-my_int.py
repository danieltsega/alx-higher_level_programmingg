#!/usr/bin/python3
"""A MyInt Module"""


class MyInt(int):
    """A class that has inherited
    an int class
    """

    def __eq__(self, other):
        """A method that checks equality
        """

        return int.__ne__(self, other)

    def __ne__(self, other):
        """A method that checks inequality
        """

        return int.__eq__(self, other)
