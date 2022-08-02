#!/usr/bin/python3
"""Module 0-lookup
Contains function that returns  list of object attributes and methods
"""


def lookup(obj):
    """return available methods and variables of an object

    Args:
        obj (object): input object

    Returns:
        list: list of object methods and variables
    """
    return dir(obj)
