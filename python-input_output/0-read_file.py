#!/usr/bin/python3
"""
Function that reads a text file
"""


def read_file(filename=""):
    """reads the file and prints it"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
