#!/usr/bin/python3
"""json deserialize"""
import json


def from_json_string(my_str):
    """json deserializer"""
    return json.loads(my_str)
