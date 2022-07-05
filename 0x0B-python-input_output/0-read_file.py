#!/usr/bin/python3
"""Mod for file reading"""


def read_file(filename=""):
    """method for reading file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            print(line, end='')
