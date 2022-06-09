#!/usr/bin/python3


def valid_string(roman_string, vstr):
    for i in roman_string:
        if i not in vstr:
            raise Exception("Malformed Roman numeral String")


def get_handler(roman_string):
    if roman_string[0] == 'I':
        return handle_I(roman_string)
    if roman_string[0] == 'V':
        return handle_V(roman_string)
    if roman_string[0] == 'X':
        return handle_X(roman_string)
    if roman_string[0] == 'L':
        return handle_L(roman_string)
    if roman_string[0] == 'C':
        return handle_C(roman_string)
    if roman_string[0] == 'D':
        return handle_D(roman_string)
    if roman_string[0] == 'M':
        return handle_M(roman_string)


def handle_I(roman_string):
    if len(roman_string) == 1:
        return 1
    if roman_string[1] == 'V':
        return 4
    if roman_string[1] == 'X':
        return 9
    return len(roman_string)


def handle_V(roman_string):
    if len(roman_string) == 1:
        return 5
    return 5 + handle_I(roman_string[1:])


def handle_X(roman_string):
    if len(roman_string) == 1:
        return 10
    if roman_string[1] == 'L':
        if len(roman_string) == 2:
            return 40
        return 40 + get_handler(roman_string[2:])
    if roman_string[1] == 'C':
        if len(roman_string) == 2:
            return 90
        return 90 + get_handler(roman_string[2:])
    val = 0
    i = 0
    while(i < len(roman_string) and roman_string[i] == 'X'):
        val += 10
        i += 1
    if i == len(roman_string):
        return val
    return val + get_handler(roman_string[i:])


def handle_L(roman_string):
    if len(roman_string) == 1:
        return 50
    return 50 + get_handler(roman_string[1:])


def handle_C(roman_string):
    if len(roman_string) == 1:
        return 100
    if roman_string[1] == 'D':
        if len(roman_string) == 2:
            return 400
        return 400 + get_handler(roman_string[2:])
    if roman_string[1] == 'M':
        if len(roman_string) == 2:
            return 900
        return 900 + get_handler(roman_string[2:])
    val = 0
    i = 0
    while(i < len(roman_string) and roman_string[i] == 'C'):
        val += 100
        i += 1
    if i == len(roman_string):
        return val
    return val + get_handler(roman_string[i:])


def handle_D(roman_string):
    if len(roman_string) == 1:
        return 500
    return 500 + get_handler(roman_string[1:])


def handle_M(roman_string):
    val = 0
    i = 0
    while(i < len(roman_string) and roman_string[i] == 'M'):
        val += 1000
        i += 1
    if i == len(roman_string):
        return val
    return val + get_handler(roman_string[i:])


def roman_to_int(roman_string):
    if type(roman_string) != str:
        return None
    roman_string = roman_string.upper()
    valid_string(roman_string, "IVXLCDM")
    return get_handler(roman_string)
