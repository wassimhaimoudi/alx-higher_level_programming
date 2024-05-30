#!/usr/bin/python3
"""This script takes in a url,
sends a request to the url and displays
the value of the variable `X-Request-Id`
in the reponse
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
