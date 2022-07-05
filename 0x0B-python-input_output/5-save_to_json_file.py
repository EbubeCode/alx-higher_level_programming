#!/usr/bin/python3
"""saves to file"""
import json


def save_to_json_file(my_obj, filename):
    """serializes an object to json and save to file"""
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
