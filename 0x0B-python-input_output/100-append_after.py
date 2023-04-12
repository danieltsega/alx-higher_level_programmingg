#!/usr/bin/python3
"""A Search and Update
Module
"""


def append_after(filename="", search_string="", new_string=""):
    """A Function that searches for a
    a special string in a file and appends
    a new string below it
    """

    new = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            new = new + line
            if search_string in line:
                new = new + new_string

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(new)
