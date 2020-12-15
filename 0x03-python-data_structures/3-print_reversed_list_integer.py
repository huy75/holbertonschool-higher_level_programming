#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
         my_list.reverse()
         print("\n".join(["{:d}".format(each) for each in my_list]))
