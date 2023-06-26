#!/usr/bin/python3
"""
Class that inherits the attributes references of class list
"""


def write_file(filename="", text=""):
    """writes to text file and retunrs num chars written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
