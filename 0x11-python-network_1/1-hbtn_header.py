#!/usr/bin/python3
""" This script takes in a url,
sends a request to the url and displays
the value of the `X-Request-Id` variable
found in the header of the response
"""


if __name__ == '__main__':
    from sys import argv
    import urllib.request

    with urllib.request.urlopen(argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))
