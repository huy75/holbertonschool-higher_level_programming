#!/usr/bin/python3
"""
This is the 2-matrix_divided module

A test file is provided in the tests directory.
To run the module: python3 -m doctest -v ./tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by a number

    matrix: a list of lists of integers or floats of the same size
    otherwise raise a TypeError exception with the message
    Each row of the matrix must have the same size
    matrix must be a matrix (list of lists) of integers/floats

    div: a number (integer or float)
    otherwise raise a TypeError exception with the message
    div must be a number
    cant be equal to 0,
    otherwise raise a ZeroDivisionError exception with the message
    division by zero
    Returns: a new matrix with divided by div, rounded to 2 decimal places
    """
    accepted = (float, int)
    mtrxErr = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, accepted):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(mtrxErr)

    mtrxLen = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(mtrxErr)
        if mtrxLen != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for each in row:
            if not isinstance(each, accepted):
                raise TypeError(mtrxErr)

    return [[round(each / div, 2) for each in row] for row in matrix]
