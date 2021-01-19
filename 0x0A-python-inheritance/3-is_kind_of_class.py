#!/usr/bin/python3
# 3-is_kind_of_class
"""
Defines a class and inherited class-checking function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class

    Arguments:
        obj (anything): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class)
