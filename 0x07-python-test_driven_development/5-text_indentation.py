#!/usr/bin/python3
"""The indetation checker module
"""


def text_indentation(text):
    """ The indentation checking
    function that returns a new
    line if it gets a ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_result = []

    a = ""

    for i in text:
        a += i

        if i in [".", "?", ":"]:
            new_result.append(a)

            a = ""
    for j in new_result:
        print("{}\n".format(j.strip(" ")))
