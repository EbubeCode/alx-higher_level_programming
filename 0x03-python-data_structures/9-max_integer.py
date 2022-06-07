#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    mx = 0
    if len(my_list) >= 1:
        mx = my_list[0]
    for i in my_list:
        if type(i) == int and mx < i:
            mx = i
    return mx
