#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print(f"Exception: {err}")
        return None
