#!/usr/bin/python3
"""Module 4-from_json_string

Contains function that converts json string into a object representation 
"""


def from_json_string(my_str):
    """Convert json string into python object

    Args:
        my_str (string): json string

    Returns:
        Python Object
    """
    import json
    return(json.loads(my_str))
