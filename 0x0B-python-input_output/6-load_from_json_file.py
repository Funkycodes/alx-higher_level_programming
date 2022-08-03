#!/usr/bin/python3
"""Module 6-load_from_json_file

Contains function that loads python objects from json file
"""
import json


def load_from_json_file(filename):
    """Read python objects from json file

    Args:
        filename (string): name of json file

    Returns:
        Object: Python Objects
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return(json.load(f))
