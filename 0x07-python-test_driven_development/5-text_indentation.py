#!/usr/bin/python3
"""
This is the 5-text_identation module

A test file is provided in the tests directory.
To run the module: python3 -m doctest -v ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    text: must be a string, otherwise raise a TypeError exception with
    the message text must be a string
    There should be no space at the beginning
    or at the end of each printed line
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for each in ".?:":
        text = (each + "\n\n").join([sentence.strip(" ")
                                    for sentence in text.split(each)])
    print(text, end="")
