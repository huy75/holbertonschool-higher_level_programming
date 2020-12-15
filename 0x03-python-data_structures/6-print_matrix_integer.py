#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    list = []
    for row in matrix:
        if row:
            list.append(" ".join(["{:d}".format(x) for x in row]))
    print("\n".join(list))
