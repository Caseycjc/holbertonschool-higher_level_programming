#!/usr/bin/python3
"""
function that writes an object to a text file using JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """writes the object to the file"""
    with open(filename, 'w', encoding="UTF8") as file:
        return json.dump(my_obj, file)

if __name__ == "__main__":
    filename = "my_list.json"
    my_list = save_to_json_file(10, filename)
    print(my_list)
    print(type(my_list))
