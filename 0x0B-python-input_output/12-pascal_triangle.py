#!/usr/bin/python3
# 12-pascal_triangle.py
"""
Defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return[]

    triangle = [[1]]

    while (len(triangle) < n):
        new_line = [1]
        prev = triangle[-1]
        for each in range(len(prev) - 1):
            new_line.append(prev[each] + prev[each + 1])
        new_line.append(1)
        triangle.append(new_line)

    return (triangle)
