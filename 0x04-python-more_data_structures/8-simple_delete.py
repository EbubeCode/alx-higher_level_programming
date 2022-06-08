#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if check_type(a_dictionary, key):
        if a_dictionary.get(key):
            del a_dictionary[key]
        return a_dictionary


def check_type(a_dictionary, key):
    return type(a_dictionary) == dict and type(key) == str
