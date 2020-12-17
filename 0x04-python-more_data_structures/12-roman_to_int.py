#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0

    if type(roman_string) is not str or roman_string is None:
        return 0

    rm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for idx in range(len(roman_string)):
        if idx == len(roman_string) - 1:
            res += rm[roman_string[idx]]
        elif rm[roman_string[idx]] >= rm[roman_string[idx + 1]]:
            res += rm[roman_string[idx]]
        else:
            res -= rm[roman_string[idx]]

    return res
