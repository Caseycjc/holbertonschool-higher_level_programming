#!/usr/bin/python3
"""
function that returns the dictionary desc
with simple data structure for JSON serialization of an object"""


def class_to_json(obj):
    """converts the object"""
    if not hasattr(obj, "__dict__"):
        return {}

    json_dict = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("__"):
            json_dict[key] = value

    return json_dict
