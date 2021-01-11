#!/usr/bin/python3
"""
This is module 6-rectangle
It defines a basic class Rectangle
"""


class Rectangle:
    """
    This class Rectangle takes two arguments.
    Example:
    x = Rectangle(2, 4)

    **Class attribute**
    number_of_instances: set to 0 initially, counts the number of objects

    **Instance attributes**
    width: private must be a non negative int
    height: private must be a non negative int

    **Instance methods**
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    __init__(self, width=0, height=0)
    area(self)
    perimeter(self)
    __str__(self)
    __repr__(self)
    __del__(self)
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Instantiate a Rectangle object
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """
        Returns area of this rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter of this rectangle.
        """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Returns string representation of Rectangle
        """
        res = ""
        if not self.__width or not self.__height:
            return res

        for idx in range(self.__height):
            res += '#' * self.__width + '\n'
        return res[:-1]

    def __repr__(self):
        """
        Returns formal string representation of Rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        Called at instance deletion.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
