#!/usr/bin/python3
"""Defines a module that add two integers"""

def add_integer(a, b=98):
    """Adds two integers a and b, else raise exception"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

