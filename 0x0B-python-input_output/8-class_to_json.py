#!/usr/bin/python3
"""module for class to json"""


def class_to_json(obj):
    """function to serialize object"""
    dic = {}
    for k in dir(obj):
        if not k.startswith('__'):
            att = getattr(obj, k)
            if type(att) in [int, bool, str, list, dict]:
                dic[k] = att
    return dic
