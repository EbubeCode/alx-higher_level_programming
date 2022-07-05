#!/usr/bin/python3
"""Mod for file writing"""


def append_write(filename="", text=""):
    """method for writing to file"""
    n_bytes = 0
    with open(filename, 'a', encoding='UTF-8') as f:
        n_bytes = f.write(text)
    return n_bytes
