#!/usr/bin/python3
"""This python script takes in github credentials
(username and password) and uses the Github API
to display id
"""


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv


    url = 'https://api.github.com/user'
    username = argv[1]
    token = argv[2]

    basic = HTTPBasicAuth(username, token)
    r = requests.get(url, auth=basic)
    _json = r.json()
    print(_json.get('id'))
