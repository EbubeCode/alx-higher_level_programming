#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if type(set_1) == set and type(set_2) == set:
        new_set = set_1 | set_2
        intersect = set_1.intersection(set_2)
        return new_set.difference(intersect)
