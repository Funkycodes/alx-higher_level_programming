#!/usr/bin/python3
"""Module 10-square
Contains class(es):
    Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class that inherits from Rectangle"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
