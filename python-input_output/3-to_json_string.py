#!/usr/bin/python3
"""
function to return the JSON rep of an object
"""


import json

def to_json_string(my_obj):
    """ returns the json rep"""
    return json.dumps(my_obj)
