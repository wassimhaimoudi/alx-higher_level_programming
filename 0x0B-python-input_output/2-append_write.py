#!/usr/bin/python3
"""This module defines the function `append_write`"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file

    Args:
        filename(str): The absoluteor relative path of the file
        text(str): the content to be appended to the end of file

    Returns:
        int: The number of characters appended.

    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
