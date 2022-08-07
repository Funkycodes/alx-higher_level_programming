#!/usr/bin/python3
"""
Module contains class Rectangle

Inherits from Base;
Inits superclass' id
Contains public attribute width, height
Prints [Rectangle] (<id>) <x>/<y> - <width>/height
Updates attributes: arg1=id, arg2=width, arg3=height, arg4=x, arg5=y 
Returns dictionary representation of attributes
"""
import base
Base = base.Base


class Rectangle(Base):
    """Define class for Geometeric shape Rectangle, inherits from Base

    Attributes:
        - Inherited :
            id
        - Instance:
            __width     __height
            __y         __x

    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        validate_attributes(self, name, value); The variant of this function
        opt in its name validates optional variables x and y
        display(self)   area(self)
        __str__(self)
        ================================
        Setters:      |  Getters:
        width(self)   |  width(self, value)
        height(self)  |  height(self, value)
        x(self)       |  x(self,value)
        y(self)       |  y(self, value)

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width: int, height: int, x: int = 0, y: int = 0, id=None):
        """Initialize all instancd variables
        Args:
            width (int): _description_
            height (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int/None, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter width

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Getter height

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @property
    def x(self):
        """Getter x

        Returns:
            int: horizontal offset
        """
        return self.__x

    @property
    def y(self):
        """Getter y

        Returns:
            int: vertical offset
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter width

        Args:
            value (int): value to set private variable to
        """
        self.validate_attribute("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter height

        Args:
            value (int): value to set private variable to
        """
        self.validate_attribute("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter x

        Args:
            value (int): value to set private variable to
        """
        self.validate_opt_attribute("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter y

        Args:
            value (int): value to set private variable to
        """
        self.validate_opt_attribute("y", value)
        self.__y = value

    def validate_attribute(self, name, value):
        """Validate compulsory attributes

        Args:
            name (string): name of parameter whose value is being validated
            value (int): value to be validated

        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0) or (value <= 0):
            raise ValueError(f"{name} must be > 0")

    def validate_opt_attribute(self, name, value):
        """Validate instance intialization optional attributes

        Args:
            name (string): name of parameter whose value is being validated
            value (int): value to be validated

        Raises:
            TypeError: if value is not an int
            ValueError: if value < 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif (value < 0) or (value < 0):
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Return value of rectangle of area

        Returns:
            int: product of width and height
        """
        return self.__height * self.__width

    def display(self):
        """Print rectangle using #(es)

        """
        print("\n" * self.__y +
              "\n".join([" " * self.x + "#" * self.__width
                         for i in range(self.__height)]))

    def __str__(self):
        """Return user friendly string representation of instance

        Returns:
            String: Author defined __str__ override
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update instance variable values
        If args: update in the following order;id, width, height, x, y
        Otherwise: set using keyworded arguments given through args
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.__width = v
                elif k == 2:
                    self.__height = v
                elif k == 3:
                    self.__x = v
                elif k == 4:
                    self.__y = v
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """Return dictionary representation of instance

        Returns:
            dict: dictionary with attributes and values serving as key, value 
            pairs respectively
        """
        diction = {}
        diction["id"] = self.id
        diction["width"] = self.width
        diction["height"] = self.height
        diction["x"] = self.x
        diction["y"] = self.y

        return diction
