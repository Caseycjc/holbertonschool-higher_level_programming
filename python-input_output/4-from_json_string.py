#!/usr/bin/python3
""" function that retuns and object represented by a json string"""


import json


def from_json_string(my_str):
    """returns the object"""
    return json.loads(my_str)
