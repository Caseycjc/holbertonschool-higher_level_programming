#!/usr/bin/python3
"""
function that writes a string to a text file and returns the number of chars written
"""


def write_file(filename="", text=""):
    """writes the string to the file"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
