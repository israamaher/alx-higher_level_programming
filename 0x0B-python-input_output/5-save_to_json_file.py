#!/usr/bin/python3
"""save object"""
import json


def save_to_json_file(my_obj, filename):
    """actually does it"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
