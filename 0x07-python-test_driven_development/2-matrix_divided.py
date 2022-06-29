#!/usr/bin/python3
"""
Module that defines a function
that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a
    matrix with the divisor div
    """
    e = 'matrix must be a matrix (list of lists) of '
    e += 'integers/floats'
    if type(matrix) != list:
        raise TypeError(e)
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    rs = len(matrix[0])
    new_matrix = []
    for ls in matrix:
        sub_mat = []
        if type(ls) != list:
            raise TypeError(e)
        if rs != len(ls):
            raise TypeError('Each row of the matrix must have the same size')
        for i in ls:
            if type(i) not in [int, float]:
                raise TypeError(e)
            sub_mat.append(round(i / div, 2))
        new_matrix.append(sub_mat)
    return new_matrix
