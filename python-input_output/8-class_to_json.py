#!/usr/bin/python3
"""
This program return the dict representation of a instance of Class.
"""


def class_to_json(obj):
    """Class to Json"""
    return obj.__dict__
