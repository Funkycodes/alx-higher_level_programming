#!/usr/bin/python3
"""Module 3-to_json_string

Contains function that converts object into a json representation 
"""
import json


def to_json_string(my_obj):
    """Return json string representation"""
    return(json.dumps(my_obj))
