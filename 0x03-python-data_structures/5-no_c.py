#!/usr/bin/python3
def no_c(my_string):
    list = [letter for letter in my_string if (letter.upper() != "C")]
    return ("".join(list))
