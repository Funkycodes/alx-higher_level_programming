#!/usr/bin/python3
"""Module 1-my_list
Contains Mylist class that inherits from and extends list class
"""


class MyList(list):
    """Extends list class"""

    def print_sorted(self):
        """print sorted instance"""
        print(sorted(self))
