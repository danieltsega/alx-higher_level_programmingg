#!/usr/bin/python3
"""A module that checks the type"""


def is_same_class(obj, a_class):
    """A function that checks
    for the type of an object
    """

    if type(obj) is a_class:
        return True
    else:
        return False
