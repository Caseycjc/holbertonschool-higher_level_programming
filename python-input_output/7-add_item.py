#!/usr/bin/python3
"""
script that adds all args to a list and then save them
"""


import sys
import json
from typing import List


def add_items_to_list(filename: str, items: List[str]):
    """adds items to the list"""
    my_list = []

    try:
        with open(filename, 'r') as file:
            my_list = json.load(file)
    except FileNotFoundError:
        pass

    my_list.extend(items)

    with open(filename, 'w') as file:
        json.dump(my_list, file)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_items_to_list("add_item.json", arguments)
