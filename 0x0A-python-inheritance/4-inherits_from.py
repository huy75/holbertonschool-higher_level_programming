#!/usr/bin/python3
# 4-inherits_from.py
"""
Defines inherited class-checking function
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Arguments:
        obj (anything): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is inherited instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class) and issubclass(type(obj), a_class)
