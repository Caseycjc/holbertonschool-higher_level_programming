#!/usr/bin/python3
"""script that fetches a website"""
import requests


def myRequest():
    """class to fetch the website"""
    x = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(x.text)))
    print("\t- content: {}".format(x.text))

if __name__ == "__main__":
    myRequest()
