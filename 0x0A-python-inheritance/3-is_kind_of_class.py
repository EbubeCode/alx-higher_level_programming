#!/usr/bin/python3
"""
A module that defines a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of a_class
    or any of its subclass
    """
    return isinstance(obj, a_class)
