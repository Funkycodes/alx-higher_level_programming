#!/usr/bin/python3
"""Module 8-class_to_json

Contains function that returns json representation of class
"""
import json


def class_to_json(obj):
    """Return json representation of obj"""
    return(json.dumps(obj.__dict__))
