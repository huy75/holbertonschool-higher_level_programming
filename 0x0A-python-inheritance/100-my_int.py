#!/usr/bin/python3
# 100-my_int.py
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A rebel: inverts == and !=
    Inherits from int
    """
    def __eq__(self, other):
        """
        returns false if two objects are equal
        """
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        """
        returns true if two objects are not equal
        """
        return super(MyInt, self).__eq__(other)
