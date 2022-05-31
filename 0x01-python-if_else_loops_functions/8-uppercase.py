#!/usr/bin/python3
def uppercase(c):
    for i in range(len(c)):
        s = c[i]
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
        print("{}".format(s), end='')
    print()
