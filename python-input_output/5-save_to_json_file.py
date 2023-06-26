#!/usr/bin/python3
"""
This program writes in a file with a JSON format
"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'w') as f:
        s = json.dump(my_obj, f)
