#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print(f"Exception: {err}", file=stderr)
        return None
