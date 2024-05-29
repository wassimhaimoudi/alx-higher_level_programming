#!/usr/bin/python3
""" This script fetches `https://alx-intranet.hbtn.io/status`
using the urllib package
"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- uft8 content: {}'.format(body.decode('utf-8')))
