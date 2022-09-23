#!/usr/bin/python3
# finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if type(list_of_integers) == list and len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
