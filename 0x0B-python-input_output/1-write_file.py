#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """
    writes to file
    -filename: name
    -text:text in file
    return: file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))
