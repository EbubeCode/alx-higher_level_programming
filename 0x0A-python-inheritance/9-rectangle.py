#!/usr/bin/python3
"""Module that defines the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that reps a Rectancle"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """implements the area declared by the
        super class"""
        return self.__width * self.__height

    def __str__(self):
        """returns the string representation of
        this rectanble"""
        return f"[Rectangle] {self.__width}/{self.__height}"
