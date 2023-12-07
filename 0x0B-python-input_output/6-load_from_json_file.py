#!/usr/bin/python3
"""loads an object from json file"""
import json

def load_from_json_file(filename):
    """
    loads an object from json file
    -filename: name of file
    -Return: an object
    """
    with open(filename) as f:
        return json.load(f)
