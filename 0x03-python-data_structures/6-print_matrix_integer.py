#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for lis in matrix:
            for i in range(len(lis)):
                end = ' '
                if i == len(lis) - 1:
                    end = ''
                print("{:d}".format(lis[i]), end=end)
            print()
