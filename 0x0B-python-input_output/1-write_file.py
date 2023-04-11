#!/usr/bin/python3
"""A File Writing Module"""


def write_file(filename="", text=""):
    """A Function that opens a file in
    writing mode and write a content
    on it
    """

    with open(filename, 'w', encoding="utf-8") as f:
        write_content = f.write(text)

        return write_content
