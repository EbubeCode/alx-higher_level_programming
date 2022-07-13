#!/usr/bin/python3
"""
Module for the class Base
"""
import os

class Base:
    """Class Base which will be the parent
    of Rectangle"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """gives the JSON string reprentation of
        list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) == list:
            x = True
            for i in list_dictionaries:
                if type(i) != dict:
                    x = False
                    break
            if x:
                return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        lis = []
        for obj in list_objs:
            lis.append(obj.to_dictionary())
        json_lis = Base.to_json_string(lis)
        filename = 'Rectangle.json'
        if 'Square' in str(cls):
            filename = 'Square.json'
        
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json_lis)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return eval(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute set"""
        base = ''
        if 'Rectangle' in str(cls):
            base = cls(3, 5)
        else:
            base = cls(3)
        if base != '':
            base.update(**dictionary)
            return base

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        filename = ''
        if 'Rectangle' in str(cls):
            filename = 'Rectangle.json'
        else:
            filename = 'Square.json'

        if not os.path.exists(filename):
            return []
        lis = []
        with open(filename, 'r', encoding='UTF-8') as f:
            json_str = f.read()
            lis_dics = Base.from_json_string(json_str)
            for o in lis_dics:
                lis.append(cls.create(**o))
        return lis
