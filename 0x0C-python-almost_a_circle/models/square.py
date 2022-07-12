#!/usr/bin/python3
"""Module that defines the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square and inherits
    the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """gives the string representation of an instance
        of this class"""
        strn = f'[Square] ({self.id}) {self.x}/{self.y} '
        strn += f'- {self.width}'
        return strn

    @property
    def size(self):
        """Getter for size property"""
        return self.height

    @size.setter
    def size(self, value):
        """Setter for size property"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes of this square"""
        x = len(args)
        if x:
            self.id = args[0]
        if x > 1:
            self.size = args[1]
        if x > 2:
            self.x = args[2]
        if x > 3:
            self.y = args[3]
        if x == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
