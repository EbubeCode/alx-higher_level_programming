#!/usr/bin/python3

def weight_average(my_list=[]):
    if type(my_list) != list:
        return
    numer = 0
    denom = 0

    for i in my_list:
        numer += i[0] * i[1]
        denom += i[1]
    if denom == 0:
        return 0
    return numer / denom
