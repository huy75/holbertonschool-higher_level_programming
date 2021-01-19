#!/usr/bin/python3
# 1-my_list.py
"""
Defines an inherited list class
"""


class MyList(list):
    """
    Assumes all the elements in the list are int
    """
    def print_sorted(self):
        """
        Function prints a sorted list
        """
        print(sorted(self))
