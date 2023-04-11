#!/usr/bin/python3
"""A JSON to Object Module"""


import json


def from_json_string(my_str):
    """A Function that takes a
    JSON representation and change
    it to a python object
    """

    new_result = json.loads(my_str)
    return new_result
