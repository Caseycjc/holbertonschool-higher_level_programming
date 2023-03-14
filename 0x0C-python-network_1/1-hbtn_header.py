#!/usr/bin/python3
"""script that takes a URL and displays a value"""
import urllib.request
import sys


def myHeader(arg):
    """class to take a URL"""
    with urllib.request.urlopen(arg) as response:
        html = response.info()
        print("{}".format(html['X-Request-Id']))

if __name__ == "__main__":
    myHeader(sys.argv[1])
