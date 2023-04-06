#!/usr/bin/python3
"""A First Name and Last Name
Printing Module
"""


def say_my_name(first_name, last_name=""):
    """ A function that return the firt
    name and last name of a given name
    argument
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
