#!/usr/bin/python3
"""Module 7-add_item

Script that save list rep of command line arguments to json file
"""
import json
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
with open("add_item.json", "w") as f:
    json.dump(argv[1:], f)
