#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for lis in matrix:
        for i in range(len(lis)):
            end = ' '
            if i == len(lis) - 1:
                end = '\n'
            print("{:d}".format(lis[i]), end=end)
