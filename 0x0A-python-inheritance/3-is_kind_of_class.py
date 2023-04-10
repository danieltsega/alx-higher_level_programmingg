#!/usr/bin/python3
"""A module that checks for the
instance of a class
"""


def is_kind_of_class(obj, a_class):
    """A function that checks for the
    instance of an object
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
