#!/usr/bin/python3
# map(func, seq) applies the function func to all the elements of the sequence seq
# map() returns an iterator
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
