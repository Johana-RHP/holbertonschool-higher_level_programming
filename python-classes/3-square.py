#!/usr/bin/python3
"""Defines the class square the instance size and its area"""


class Square:
    """
    Define a square
    Args:
        size : size of a side in square
    Functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """Initializes square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area
        Returns:
            area
        """
        return (self.__size)**2
