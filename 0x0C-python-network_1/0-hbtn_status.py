#!/usr/bin/python3
"""Pthon script that fetches a webpage"""
import urllib.request


def my_Status():
    """class to fetch the webpage"""
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

if __name__ == "__main__":
    my_Status()
