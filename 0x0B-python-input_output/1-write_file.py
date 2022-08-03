#!/usr/bin/python3
"""Module 1-write_file

Contains function that writes to file
"""


def write_file(filename="", text=""):
    """Write text to filename"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
