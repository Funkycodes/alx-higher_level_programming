#!/usr/bin/python3
"""
Module contains class Square

Inherits from Rectangle;
Inits superclass' id, width (as size), height (as size), x, y
Contains public attribute size
Prints [Square] (<id>) <x>/<y> - <size>
Updates attributes: arg1=id, arg2=size, arg3=x, arg4=y
Returns dictionary representation of attributes
"""

from models import rectangle

Rectangle = rectangle.Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance

        Args:
            size (int): value of width and height of square
            x (int, optional): Horizontal offset. Defaults to 0.
            y (int, optional): Vertical offset. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size Getter

        Returns:
            int : size of square which is represented by width or height
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter size: Assign size to inherited variables

        Args:
            value (int): size; height and width of squares
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return user friendly string representation of instance

        Returns:
            String: Author defined __str__ override
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - \
{self.width}")

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                elif k == 3:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation of instance

        Returns:
            dict: dictionary with attributes and values serving as key, value
            pairs respectively
        """

        diction = {}
        diction['id'] = self.id
        diction['size'] = self.size
        diction['x'] = self.x
        diction['y'] = self.y

        return diction
