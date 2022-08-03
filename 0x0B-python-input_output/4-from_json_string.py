#!/usr/bin/python3
"""Module 4-from_json_string

Contains function that converts json string into a object representation 
"""
import json


def from_json_string(my_str):
    """Return object"""
    return (json.loads(my_str))
