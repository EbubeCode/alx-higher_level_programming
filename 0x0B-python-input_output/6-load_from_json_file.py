#!/usr/bin/python3
"""loads json object"""
import json


def load_from_json_file(filename):
    """creates an object by loading from json file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.load(f)
