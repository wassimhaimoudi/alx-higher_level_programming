#!/usr/bin/python3
"""This script fetches
`https://alx-intranet.hbtn.io/status`
"""
if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.content)))
    print("\t- content: {}".format(r.text))
