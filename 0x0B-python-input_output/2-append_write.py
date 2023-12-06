#!/usr/bin/python3
"""appand function """


def append_write(filename="", text=""):
    with open(filename, mode="a+", encoding="UTF8") as f:
        return f.write(text)
