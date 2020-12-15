#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        print("\n".join(["{:d}".format(each) for each in my_list]))
