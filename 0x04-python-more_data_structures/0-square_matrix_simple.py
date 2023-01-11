#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = [ [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0] ]
    y = len(matrix)
    for i in range(y):
        m[i] = matrix[i] ** 2
        print(m)
