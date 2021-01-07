#!/usr/bin/python3
"""
This is the 0-add_integer module.

A test file is provided in the tests directory.
To run the module: python3 -m doctest -v ./tests/0-add_integer.txt
"""


def add_integer(a, b=98):
    """
    Adds two integers
    a: should be an integer, a float will be cast to an integer
    b: should be an integer, a float will be cast to an integer

    Return:
    a + b. Or raise an error.
    """
    accepted = (float, int)
    if not isinstance(a, accepted):
        raise TypeError("a must be an integer")
    if not isinstance(b, accepted):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
