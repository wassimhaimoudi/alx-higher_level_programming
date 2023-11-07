#!/usr/bin/python3
"""This module defines the function `read_file`"""


def read_file(filename):
    """
    Function that reads tesxt file using UTF-8 encoding
    and prints it out to the stdout.

    Args:
        filename(str): The absolute or relative path to the file

    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
