#!/usr/bin/python3
"""Module 2-append_write

Contains function that appends to file
"""


def append_write(filename="", text=""):
    """Append text to existing file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
