#!/usr/bin/python3
"""
Defines a module that add two integers
The module will be tested with doctest
This test will be reference from a test file
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b, else raise exception
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
