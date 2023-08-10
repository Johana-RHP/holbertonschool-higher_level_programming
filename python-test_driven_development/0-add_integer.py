!/usr/bin/python3
"""
Contains a method that returns the add of two int
"""


def add_integer(a, b=98):
    """
    Returns a + b as int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
