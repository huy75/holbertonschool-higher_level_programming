#!/usr/bin/python3
# 101-add_attribute.py
"""
Module add_attribute method
"""


def add_attribute(obj, name, value):
    """
    Checks if possible to add a new attribute to an object
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
