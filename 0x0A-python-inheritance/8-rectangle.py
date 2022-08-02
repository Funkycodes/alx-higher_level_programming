#!/usr/bin/python3
"""Module 7-base_geometry
Contains Class(es):
    BaseGeometry
"""


class BaseGeometry():
    """Base Class for geometrical objects"""

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits froom BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
