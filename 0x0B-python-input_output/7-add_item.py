#!/usr/bin/python3
"""loads adds saves json to file"""
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

listarg= list(sys.argv[1:])
try:
    jsonList = load_from_json_file("add_item.json")
except Exception:
    jsonList = []

jsonlist.extend(listarg)
save_to_json_file(jsonList, "add_item.json")
