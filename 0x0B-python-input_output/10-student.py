#!/usr/bin/python3
"""module that defines a student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of a student"""
        if type(attrs) == list:
            dic = {}
            for i in attrs:
                if type(i) != str:
                    dic = {}
                elif i in ['first_name', 'last_name', 'age']:
                    dic[i] = getattr(self, i)
            if dic != {}:
                return dic
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age}
