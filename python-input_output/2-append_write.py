#!/usr/bin/python3
"""
Function that returns True/False if obj is a type of a_class
"""


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
