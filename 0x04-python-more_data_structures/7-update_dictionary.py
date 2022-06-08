#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if type(a_dictionary) == dict and type(key) == str:
        a_dictionary[key] = value
        return a_dictionary
