#!/usr/bin/python3
""" This script takes in a url,
sends a request to the url and displays
the body ofthe response(decoded in utf-8)
"""
import urllib.request
import urllib.error
from sys import argv


url = argv[1]
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
