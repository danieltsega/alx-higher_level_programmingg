#!/usr/bin/python3
"""A List Module"""


class MyList(list):
    """A class that inherits a
    list class
    """

    def __init__(self):
        """An initialized function
        for the class
        """

        list.__init__(self)

    def print_sorted(self):
        """A method that prints
        a sorted list
        """

        print(sorted(self))
