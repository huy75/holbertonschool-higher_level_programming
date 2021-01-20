#!/usr/bin/python3
# 2-append_write.py
"""
Defines a file-appending function.
"""


def append_write(filename="", text=""):
    """
    Append a string to a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
