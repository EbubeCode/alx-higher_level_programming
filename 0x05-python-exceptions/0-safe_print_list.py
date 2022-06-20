#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(0, x):
            print(f"{my_list[i]}", end='')
            a += 1
        print()
        return a
    except Exception:
        print()
        return a
