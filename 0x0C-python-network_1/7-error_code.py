#!/usr/bin/python3
"""script that prints an error code"""
from sys import argv
import requests


def errorcode():
    """class to print error code"""
    result = requests.get(argv[1])
    if result.status_code > 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)

if __name__ == "__main__":
    errorcode()
