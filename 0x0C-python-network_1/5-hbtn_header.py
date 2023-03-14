#!/usr/bin/python3
"""script that sends request to a URL and displays the value of a variable"""
import requests
import sys


def myRequestX(arg):
    """class to request the URL and display the value"""
    x = requests.get(arg)
    print("{}".format(x.headers.get('X-Request-Id')))

if __name__ == "__main__":
    myRequestX(sys.argv[1])
