#!/usr/bin/python3
# 0-lookup.py
"""
Defines an object attribute lookup function
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return (dir(obj))
