#!/usr/bin/python3
# 100-append_after.py
"""
Defines a text file insertion function.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The file name.
        search_string (str): The searched string.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as read_file:
        for line in read_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as write_file:
        write_file.write(text)
