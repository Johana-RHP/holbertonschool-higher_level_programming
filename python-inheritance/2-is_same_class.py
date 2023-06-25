#!/usr/bin/python3
"""
Returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Use type() to get specific class
    Return:
    Returns True if the object is exactly an instance of the
    specified class and False otherwise
    """
    return type(obj) == a_class
