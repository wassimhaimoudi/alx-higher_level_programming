#!/usr/bin/python3
"""This script takes in a letter
and sends a POST request to
`http://0.0.0.0:5000/search_user`
with the letter as a param
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    data = {}
    if len(argv) == 1:
        data.setdefault('q', '')
    else:
        data.setdefault('q', argv[1])
    r = requests.post(url, data=data)
    try:
        if (_json := r.json()) == {}:
            print('No result')
        else:
            id = _json.get('id')
            name = _json.get('name')
            print(f'[{id}] {name}')
    except Exception:
        print('Not a valid JSON')
