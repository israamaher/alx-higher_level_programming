#!/usr/bin/python3
import json
"""loads an object from json file"""


def load_from_json_file(filename):
    """
    loads an object from json file
    -filename: name of file
    -Return: an object
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return(json.load(f))
