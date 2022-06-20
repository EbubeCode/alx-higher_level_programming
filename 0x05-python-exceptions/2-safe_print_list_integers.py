#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a = 0
    b = 0
    while a < x:
        try:
            print("{:d}".format(my_list[a]), end='')
            a += 1
            b += 1
        except Exception as err:
            if type(err) == IndexError:
                raise
            a += 1
    print()
    return b
