#!/usr/bin/python3
"""
function that creates an object from a JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
