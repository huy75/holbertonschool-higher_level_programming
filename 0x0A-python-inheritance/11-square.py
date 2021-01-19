#!/usr/bin/python3
# 11-square.py
"""
Defines a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class square, subclass from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the representation of Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
