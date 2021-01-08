#!/usr/bin/python3
"""
This is the 4-print_square module

A test file is provided in the tests directory.
To run the module: python3 -m doctest -v ./tests/4-print_square.txt
"""


def print_square(size):
    """
    prints a square with the character #

    size: the size length of the square
    must be an integer, otherwise raise a TypeError exception with the message
    size must be an integer
    if size is less than 0, raise a ValueError exception with the message
    size must be >= 0
    if size is a float and is less than 0, raise a TypeError exception
    with the message size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (size == 0):
        print("", end="")
    else:
        print("\n".join(["#" * size for each in range(size)]))
