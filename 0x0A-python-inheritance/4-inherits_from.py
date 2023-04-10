#!/usr/bin/python3
"""A Module that checks
the instance of an object
"""


def inherits_from(obj, a_class):
    """A function that returns the
    instance of an object
    """

    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
