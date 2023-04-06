#!/usr/bin/python3
"""The square printing Module
"""


def print_square(size):
    """A function tha prints a square
    given the size as an argument
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
