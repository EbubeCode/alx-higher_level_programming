#!/usr/bin/python3
"""
Module that defines the class
BaseGeometry
"""


class BaseGeometry:
    """defines method area(self)"""

    def area(self):
        """unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if value is None or type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
