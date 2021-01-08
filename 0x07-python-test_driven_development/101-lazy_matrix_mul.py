#!/usr/bin/python3
"""
This is the 101-lazy_matrix_mul module
matrix multiplication with NumPy

A test file is provided in the tests directory
To run the module: python3 -m doctest ./tests/101-lazy_matrix_mul.txt
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiply matrixes with numpy

    m_a: must be a matrix of numbers
    m_b: must be a matrix of numbers
    Returns: a matrix, the product of the arguments
    """

    matrix = np.dot(m_a, m_b)
    return matrix
