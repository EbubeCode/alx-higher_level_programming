#!/usr/bin/python3

def max_integer(my_list=[]):
    if not len(my_list):
        return None
    mx = 0
    for i in my_list:
        if  type(i) != int:
            raise TypeError()
        if mx < i:
            mx = i
    return mx
