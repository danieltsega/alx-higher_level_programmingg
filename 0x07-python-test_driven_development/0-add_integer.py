#!/usr/bin/python3
"""A module that has a function
that returns the addition of two
numbers
"""


def add_integer(a, b=98):
    """A function that adds two numbers
    that are integers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an intege")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return a + b
