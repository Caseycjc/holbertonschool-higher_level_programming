#!/usr/bin/python3
"""script that takes a URL and email and sends a POST request"""
import requests
import sys


def myEmail(args, email):
    """class to fetch the email"""
    data = {'email': email}
    x = requests.post(args, data=data)
    print("{}".format(x.text))

if __name__ == "__main__":
    myEmail(sys.argv[1], sys.argv[2])
