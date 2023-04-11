#!/usr/bin/python3
"""File Appending Module"""


def append_write(filename="", text=""):
    """A Function that opens a file
    in append mode and apends a content
    to it
    """

    with open(filename, 'a', encoding="utf-8") as f:
        append_content = f.write(text)

        return append_content
