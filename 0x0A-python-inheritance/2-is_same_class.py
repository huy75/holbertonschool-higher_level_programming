#!/usr/bin/python3
# 2-is_same_class.py
"""
Defines a class-checking function
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class
    """
    return obj.__class__ == a_class
