#!/usr/bin/python3

def common_elements(set_1, set_2):
    if type(set_1) == set and type(set_2) == set:
        return set_1.intersection(set_2)
