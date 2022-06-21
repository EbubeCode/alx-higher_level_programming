#!/usr/bin/python3
"""This module contains a Square class which has
a private attribute __size"""


class Square:
    """A square class with the attribute __size"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Calculates the area of the square"""
        x = self.__size
        return x * x

    @property
    def size(self):
        """Getter for __size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
