#!/usr/bin/python3
""" This script fetches `https://alx-intranet.hbtn.io/status`
using the urllib package
"""


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    response = response.read()

if __name__ == '__main__':
    print('Body response:')
    print(f'\t- type: {type(response)}')
    print(f'\t- content: {response}')
    print(f'\t- uft8 content: {response.decode("utf")}')
