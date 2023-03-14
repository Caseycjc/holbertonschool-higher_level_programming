#!/usr/bin/python3
"""
a Python script that fetches 'https://intranet.hbtn.io/status'
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
