#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) == dict:
        dic = sorted(a_dictionary.items())
        for i in dic:
            print(f"{i[0]}: {i[1]}")
