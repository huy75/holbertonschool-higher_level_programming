#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if 0 <= idx < len(my_list):
            newList = my_list[:]
            newList[idx] = element
            return newList
        else:
            return my_list
