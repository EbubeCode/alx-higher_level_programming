#!/usr/bin/python3
"""
Module that defines the method is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if an object is exactlyy an instance of
    the specified class
    """
    return type(obj) == a_class
