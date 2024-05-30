#!/usr/bin/python3
"""This script takes in a url and an email address,
sends a POST request to the passed url with the email
as a param, and finally displays the response body
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    data = {
                'email': argv[2]
            }
    r = requests.post(url, data=data)
    print(r.text)
