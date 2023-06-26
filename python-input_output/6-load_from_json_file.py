#!/usr/bin/python3
"""
This program reads files .json and convert to types of python
"""


import json


def load_from_json_file(filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'r') as f:
        return json.load(f)
