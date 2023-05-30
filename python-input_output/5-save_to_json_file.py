#!/usr/bin/python3
"""
function that writes an object to a text file using JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """writes the object to the file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
