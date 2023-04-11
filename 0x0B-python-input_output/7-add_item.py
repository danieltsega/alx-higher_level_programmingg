#!/usr/bin/python3
"""A Command line argument
to a json file Module
"""


import sys
import os.path


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

arg_list = []
if os.path.exists("add_item.json") is True:
    arg_list = load_from("add_item.json")

for i in sys.argv[1:]:
    arg_list.append(i)

save_to(arg_list, "add_item.json")
