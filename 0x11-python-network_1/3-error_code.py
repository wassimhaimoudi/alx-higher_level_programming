#!/usr/bin/python3
"""This module takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
from sys import argv

url = argv[1]
try:
    with urllib.request.urlopen(url) as resp:
        print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
