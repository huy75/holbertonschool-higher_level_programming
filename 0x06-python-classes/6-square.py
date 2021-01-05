#!/usr/bin/python3
"""
This is module 6-square
It defines a class that defines a Square
"""


class Square:
    """
    This class Square takes two private attributes:
    size (int): len of one side
    position (tuple): top left corner

    Example:
    x = Square(2)

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiate a Square object
        Arguments:
            size (int): len of size of square
            position (tuple): position to print
        """
        self.size = size
        self.position = position

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
        Check if the input value is a positive or null
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        getter for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Returns the area of a square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints the square
        """
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        print("\n".join([" " * self.__position[0] + "#" * self.__size
                         for each in range(self.__size)]))
