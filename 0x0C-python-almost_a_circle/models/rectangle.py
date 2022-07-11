#!/usr/bin/python3
"""
Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        w = self.__width
        h = self.__height

        for i in range(h):
            for j in range(w):
                print('#', end='')
            print()

    @staticmethod
    def __check_int(value, attr):
        """method to check int"""
        if type(value) != int:
            raise TypeError(f"{attr} must be an integer")

    @property
    def width(self):
        """Getter for __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for __width"""
        self.__check_int(value, "width")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height"""
        self.__check_int(value, "height")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for __x"""
        self.__check_int(value, "x")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for __y"""
        self.__check_int(value, "y")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
