#!/usr/bin/python3
"""
Module that returns the list of available attributes and methods of an object
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
