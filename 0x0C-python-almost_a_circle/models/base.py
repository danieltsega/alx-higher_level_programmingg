#!/usr/bin/python3
""" The Base Class Module"""


class Base:
    """A base class that is the
    base of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """A constructor method"""

        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
