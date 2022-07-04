#!/usr/bin/python3
"""
A module that contains the method lookup
"""


def lookup(obj):
    """
    returns the list of available attributes and
    methods of an object
    """
    return dir(obj)
