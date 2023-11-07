#!/usr/bin/python3
"""this module defines the function `write_file`"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file in UFT8
    Args:
        filename(str): The absolute or relative path of the file
        text(str): The text content to be written in the file

    Returns:
        int: The number of characters read
    """
    with open(filename, 'w', encoding="utf-8") as f:
        c = f.write(text)
        return (c)
