#!/usr/bin/python3
"""This module contains a Square class which has
a private attribute __size"""


class Square:
    """A square class with the attribute __size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the square"""
        x = self.__size
        return x * x

    def my_print(self):
        """prints in stdout the square with the char #"""
        s = self.__size
        x = self.__position[0]
        if s == 0:
            print()
        else:
            for i in range(s):
                print(' '*x, end='')
                for j in range(s):
                    print('#', end='')
                print()

    @property
    def position(self):
        """Getter for __position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for __position attribute"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
