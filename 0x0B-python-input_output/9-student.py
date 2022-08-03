#!/usr/bin/python3
"""Module 9-student

Contains class(es):
    Student
"""
import json


class Student:
    """Student Class
    """

    def __init__(self, first_name, last_name, age):
        """Initialize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of instance"""
        return(json.dumps(self.__dict__))
