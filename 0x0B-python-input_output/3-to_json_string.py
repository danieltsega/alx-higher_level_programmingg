#!/usr/bin/python3
"""A Object to JSON Module"""


import json


def to_json_string(my_obj):
    """A function that takes a
    python object and returns
    a JSON representation
    """

    new_result = json.dumps(my_obj)
    return new_result
