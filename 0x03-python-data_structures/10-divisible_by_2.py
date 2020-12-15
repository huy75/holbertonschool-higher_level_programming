#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        return ([each % 2 == 0 for each in my_list])
    return None
