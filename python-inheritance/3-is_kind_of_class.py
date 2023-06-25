#!/usr/bin/python3
"""
Module that returns True/False if obj is an instance of a_class
"""


def is_kind_of_class(obj, a_class):
    """
    Use isinstance() to get class and any parent classes too
    Return:
    Return True if the object is an instance of, or if the object is an
    instance of a class that inherited from the specified class
    otherwise False
    """
    return isinstance(obj, a_class)
