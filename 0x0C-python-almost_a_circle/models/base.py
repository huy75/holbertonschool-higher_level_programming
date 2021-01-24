#!/usr/bin/python3
"""
This is module base.py
It defines a basic class Base
"""


class Base:
    """
    This class Base takes one argument.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiate a Base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
