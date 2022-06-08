#!/usr/bin/python3

def best_score(a_dictionary):
    if type(a_dictionary) == dict and len(a_dictionary) > 0:
        max = 0
        idx = 0
        for i in a_dictionary.keys():
            if idx == 0:
                max = i
                idx += 1
            if a_dictionary[i] > a_dictionary[max]:
                max = i
        return max
