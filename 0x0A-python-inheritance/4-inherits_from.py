#!/usr/bin/python3
"""
Module that defines the function
inherits_from
"""


def inherits_from(obj, a_class):
    """
    checks if obj is an instance of
    a class that extends a_class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
