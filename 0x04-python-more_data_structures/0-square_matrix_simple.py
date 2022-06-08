#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        lis = list(map(lambda x: x*x, i))
        new_matrix.append(lis)
    return new_matrix
