#!/usr/bin/python3
"""
reads a text file
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
