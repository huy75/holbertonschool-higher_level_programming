#!/usr/bin/python3
# 7-base_geometry.py
"""
Defines a class BaseGeometry
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """

    def area(self):
        """
        Not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): positive integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
