#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Use issubclass() to get what object is a subclass of
    Return:
    True if the object is an instance of a class that inherited
    from the specified class or False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
