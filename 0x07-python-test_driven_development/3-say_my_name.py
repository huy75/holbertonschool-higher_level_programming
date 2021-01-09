#!/usr/bin/python3
"""
This is the module 3-say_my_name
A test file is provided in the test directory
To run the module: python3 -m doctest -v ./tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    first_name, last_name are string
    otherwise raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
    """
    if first_name is None or type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
