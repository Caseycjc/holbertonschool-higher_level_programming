#!/usr/bin/python3
"""Pthon script that fetches a webpage"""
import urllib.request


def myStatus():
    """class to fetch the webpage"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body responce:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

if __name__ == "__main__":
    myStatus()
