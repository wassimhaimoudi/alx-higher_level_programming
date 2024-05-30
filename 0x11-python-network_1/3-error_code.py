#!/usr/bin/python3
"""Fetches a url and handles errors
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.error
    from sys import argv
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
