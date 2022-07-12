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
        """shows a graphical representation of this
        rectangle using the character #"""
        w = self.__width
        h = self.__height

        print('\n' * self.x, end='')
        for i in range(h):
            print(' ' * self.y, end='')
            for j in range(w):
                print('#', end='')
            print()

    def __str__(self):
        """returns the string representation of this
        rectangle"""
        strn = '[Rectangle] (' + str(self.id) + ') '
        strn += str(self.x) + '/' + str(self.y) + ' - '
        strn += str(self.width) + '/' + str(self.height)
        return strn

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

    def update(self, *args, **kwargs):
        """method that assigns an argument to each
        attribute"""
        x = len(args)
        if x:
            self.id = args[0]
        if x > 1:
            self.width = args[1]
        if x > 2:
            self.height = args[2]
        if x > 3:
            self.x = args[3]
        if x > 4:
            self.y = args[4]
        if x == 0:
            for key, value in kwargs.items():
                if key == 'height':
                    self.height = value
                elif key == 'width':
                    self.width = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

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
