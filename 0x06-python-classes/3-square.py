#!/usr/bin/python3
"""
This is module 3-square
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
        Check if the input value is a positive or null digit
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of a square
        """
        return (self.__size * self.__size)
