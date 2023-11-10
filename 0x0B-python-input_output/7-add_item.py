#!/usr/bin/python3
"""This module contains a script to add itmes to a list"""

if __name__ == '__main__':
    import sys

    load = __import__('6-load_from_ json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = 'add_item.json'
    try:
        my_list = load(filename)
    except FileNotFoundError:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, filename)
