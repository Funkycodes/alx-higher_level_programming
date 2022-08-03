#!/usr/bin/python3
"""Module 5-save_to_json_file

Contains function that saves json rep of object to json file 
"""
import json


def save_to_json_file(my_obj, filename):
    """Save my-obj to json file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
