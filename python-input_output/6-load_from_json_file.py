#!/usr/bin/python3
"""
function that creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """creates the object"""
    with open(filename, 'r') as file:
        return json.load(file)
