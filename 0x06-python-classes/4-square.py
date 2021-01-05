#!/usr/bin/python3
"""
This is module 4-square
It defines a basic class Square
"""


class Square:
    """
    This class Square takes one argument.

    Example:
    x = Square(2)

    """
    def __init__(self, size=0):
        """
        Instantiate a Square object
        """
        self.__size = size

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size
        Check if the input value is a positive or null digit
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of a square
        """
        return (self.__size * self.__size)
