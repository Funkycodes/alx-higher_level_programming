#!/usr/bin/python3
"""Module 3-is_kind_of_class
Contains function that checks if object is an instance of a class or any class it inherits from
"""


def is_kind_of_class(obj, a_class):
    """"Check if obj is an instance of a_class"""
    return isinstance(obj, a_class)
