#!/usr/bin/python3
"""
This is the 100-matrix_mul module

A test file is provided in the tests directory.
To run the module: python3 -m doctest -v ./tests/2-matrix_mul.txt
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices

    m_a, m_b: mactrices of numbers

    Returns: the resulting matrice, if it's possible
    """

    accepted = (float, int)

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        m = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError(m + " must be a list")

    for each in m_a:
        if not isinstance(each, list):
            raise TypeError('m_a must be a list of lists')
    for each in m_b:
        if not isinstance(each, list):
            raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    for row in m_a:
        for each in row:
            if not isinstance(each, accepted):
                raise TypeError('m_a should contain only integers or floats')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')

    for row in m_b:
        for each in row:
            if not isinstance(each, accepted):
                raise TypeError('m_b should contain only integers or floats')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    rowsMa = len(m_a)
    colsMa = len(m_a[0])
    rowsMb = len(m_b)
    colsMb = len(m_b[0])

    if colsMa != rowsMb:
        raise ValueError("m_a and m_b can't be multiplied")

    # create an empty result matrice
    result = [[0 for row in range(colsMb)] for col in range(rowsMa)]
    for i in range(rowsMa):
        for j in range(colsMb):
            for k in range(colsMa):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
