#!/usr/bin/python3

"""returns an object (Python data structure) represented by a JSON string"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by JSON string"""
    obj = json.loads(my_str)
    return obj
