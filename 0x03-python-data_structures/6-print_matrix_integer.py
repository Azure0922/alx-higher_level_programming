#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for column in matrix:
        for i in range(3):
            print("{a}".format(a=column[i]))
