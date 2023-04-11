#!/usr/bin/python3
"""A Object to JSON in
File MOdule
"""


import json


def save_to_json_file(my_obj, filename):
    """A Function that gets a python object
    and convert it to JSON and save it on a
    file
    """

    with open(filename, 'w') as f:
        write_content = json.dump(my_obj, f)
