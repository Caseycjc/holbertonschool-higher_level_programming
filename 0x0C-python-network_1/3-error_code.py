#!/usr/bin/python3
"""script that takes in a URL and displays the body of the response"""
import urllib.request
import sys


def myError(url):
    """class to take the URL and display a response"""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

if __name__ == "__main__":
    myError(sys.argv[1])
