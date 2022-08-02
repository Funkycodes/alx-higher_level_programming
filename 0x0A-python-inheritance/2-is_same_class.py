#!/usr/bin/python3
"""Module 2-is_same_class
Contains that checks if an object is particular object type
"""


def is_same_class(obj, a_class):
    """Return true if obj is of type a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False
