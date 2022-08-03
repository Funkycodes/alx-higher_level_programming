#!/usr/bin/python3
"""Module 10-student

    Contains class(es):
        Student
    """
import json


class Student:
    """Class to represent students"""

    def __init__(self, first_name, last_name, age):
        """Initialize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of instance
        """
        if attrs == None:
            return(self.__dict__)
        else:
            _dict = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    _dict[att] = self.__dict__[att]
            return(_dict)
