#!/usr/bin/python3
"""This script fetches https://intranet.hbtn.io/status.
"""
import urllib.request


if __name__ == '__main__':
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
            body = resp.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        pass
