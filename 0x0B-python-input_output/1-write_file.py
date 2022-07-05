#!/usr/bin/python3
"""Mod for file writing"""


def write_file(filename="", text=""):
    """method for writing to file"""
    n_bytes = 0
    with open(filename, 'w', encoding='UTF-8') as f:
        n_bytes = f.write(text)
    return n_bytes
