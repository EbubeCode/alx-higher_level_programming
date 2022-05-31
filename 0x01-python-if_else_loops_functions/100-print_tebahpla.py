#!/usr/bin/python3

c = 0
for i in range(122, 96, -1):
    if c % 2 != 0:
        i -= 32
    print("{}".format(chr(i)), end='')
    c += 1
