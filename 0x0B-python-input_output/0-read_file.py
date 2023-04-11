#!/usr/bin/python3
"""A File reading Module"""


def read_file(filename=""):
    """A Function that opens a file
    in a read mode and prints the
    content of the file
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print_data = f.read()

        print(print_data, end="")
