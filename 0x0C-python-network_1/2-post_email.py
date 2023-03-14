#!/usr/bin/python3
"""script to take a URL and email and send a POST request"""
import urllib.request
import urllib.parse
from sys import argv


def myEmail(args, email):
    """class to fetch the URL and email to send the POST request"""
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(args, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))

if __name__ == "__main__":
    myEmail(argv[1], argv[2])
