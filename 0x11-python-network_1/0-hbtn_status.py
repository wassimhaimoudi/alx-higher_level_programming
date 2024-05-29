#!/usr/bin/python3
""" This script fetches `https://alx-intranet.hbtn.io/status`
using the urllib package
"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()

        print('Body response:')
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
        print(f'\t- uft8 content: {body.decode("utf")}')
    except Exception:
        pass
