#!/usr/bin/python3
"""A Attribute Module
"""


def add_attribute(obj, name, value):
    """A Function that adds an attribute
    for a dictionary instance
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)

    else:
        raise TypeError("can't add new attribute")
