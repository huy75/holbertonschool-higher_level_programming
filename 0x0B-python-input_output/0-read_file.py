#!/usr/bin/python3
# 0-read_file.py
"""
Defines a text file-reading function.
"""


def read_file(filename=""):
    """
    Print the contents of a UTF8 text file to stdout.

    Args:
        filename (str): name of file to be opened.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
