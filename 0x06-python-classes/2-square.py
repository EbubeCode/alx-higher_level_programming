#!/usr/bin/python3
"""This module contains a Square class which has
a private attribute __size"""


class Square:
    """A square class with the attribute __size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
