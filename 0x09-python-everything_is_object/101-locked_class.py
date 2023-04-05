#!/usr/bin/python3
"""A Locked Class Module"""


class LockedClass:
    """ A class that has a
    locked attribute
    """

    __slots__ = "first_name"
    
    def __init__(self):
        """An initialising method
        that don't do anything
        """

        pass

