#!/usr/bin/python3
"""
This module defines a method that prints
a square using the character '#'
"""


def print_square(size):
    """
    This method prints a square of size 'size'
    with the character '#'
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    strn = ''
    for i in range(size):
        for j in range(size):
            strn += '#'
        strn += '\n'
    print(strn)
