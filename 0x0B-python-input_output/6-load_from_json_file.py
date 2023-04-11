#!/usr/bin/python3
"""A JSON to Object
Module
"""


import json


def load_from_json_file(filename):
    """A Function that takes a json
    file and convert it to a python
    object
    """

    with open(filename, 'r') as f:
        new_result = json.load(f)
        return new_result
