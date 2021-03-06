#!/usr/bin/python3
"""
This is module 9-rectangle
It defines a basic class Rectangle
"""


class Rectangle:
    """
    This class Rectangle takes two arguments.
    Example:
    x = Rectangle(2, 4)

    **Class attribute**
    number_of_instances: set to 0 initially, counts the number of objects
    print_symbol: any type

    **Instance attributes**
    width: private must be a non negative int
    height: private must be a non negative int

    **Static method**
    bigger_or_equal(rect_1, rect_2)

    **Class method**
    square(cls, size=0)

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
    print_symbol = "#"

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
            res += str(self.print_symbol) * self.__width + '\n'
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares 2 rectangles
        Arguments:
            rect_1: a Rectangle
            rect_2: a Rectangle
        Returns:
            the  Rectangle with bigger area, rect_1 if tie
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square
        Arguments:
            size: size of square
        Returns:
            a Rectangle with width==weight
        """
        return cls(size, size)
