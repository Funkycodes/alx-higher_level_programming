#!/usr/bin/python3
"""Module 4-inherits_from
Contains function that checks whether an object is a subclass of another class
"""


def inherits_from(obj, a_class):
    """Check if obj is of a type that inherits from a_class"""

    return issubclass(type(obj), a_class)
