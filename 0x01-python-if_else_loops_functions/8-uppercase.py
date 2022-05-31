#!/usr/bin/python3
def uppercase(c):
    for i in range(len(c)):
        e = ''
        s = c[i]
        if i == len(c) - 1:
            e = '\n'
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
            print("{}".format(s), end=e)
        else:
            print("{}".format(s), end=e)
