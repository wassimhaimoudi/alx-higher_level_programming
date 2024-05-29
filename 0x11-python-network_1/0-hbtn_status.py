#!/usr/bin/python3
""" This script fetches https://intranet.hbtn.io/status
using the package urllib
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    html = resp.read()

print("Body response:")
print("\t- type: {}".format(type(html))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
