#!/usr/bin/python3
"""This script takes in a url.
sends a request to the url, and displays
the body of the response.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
