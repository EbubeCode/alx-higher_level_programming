#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if type(a_dictionary) != dict:
        return
    lis = []
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            lis.append(i)
    for i in lis:
        del a_dictionary[i]
    return a_dictionary
