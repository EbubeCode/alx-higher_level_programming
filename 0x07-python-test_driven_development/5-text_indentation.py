#!/usr/bin/python3
"""
This module defines a function 'text_indentation'
that prints the parameter 'text' in a particular
format
"""


def text_indentation(text):
    """
    prints the string 'text' with 2 new lines arter each
    of these characters: . , ? and :
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    for i in text:
        e = ''
        if i in '.,?:':
            e = '\n\n'
        print(i, end=e)
