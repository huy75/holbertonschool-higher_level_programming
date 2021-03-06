#!/usr/bin/python3
"""
This is module 1-rectangle
It defines a basic class Rectangle
"""


class Rectangle:
    """
    This class Rectangle takes two arguments.

    Example:
    x = Rectangle(2, 4)
    """
    def __init__(self, width=0, height=0):
        """
        Instantiate a Rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        Check if the input value is a positive or null integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        Check if the input value is a positive or null integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
