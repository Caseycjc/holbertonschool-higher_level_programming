#!/usr/bin/python3
"""
function that appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """appends a string to EOF"""
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)

    return num_characters_added
