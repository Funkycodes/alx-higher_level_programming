#!/usr/bin/python3
"""Module 0-read_file
Contains function that reads and prints file contents
"""


def read_file(filename=""):
    """Print file contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read().strip('\n'))
