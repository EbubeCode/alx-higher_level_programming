#!/usr/bin/python3
"""Module that defines the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass of Rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """overides the implementation of Rectangle"""
        return self.__size ** 2
