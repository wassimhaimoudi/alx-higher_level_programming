#!/usr/bin/python3
""" This script takes in a url and an email, sends a POST
request to the passed url with the emailas a parameter
and displays the body of the response(decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = {}
    data['email'] = email
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as resp:
        print("Your email is: {}".format(resp.read().decode('utf-8')))
