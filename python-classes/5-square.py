#!/usr/bin/python3
"""Defines the class square the instance size and its area"""


class Square:
    """
    Define a square
    Args:
        size : size of a side in square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area8self)
    """
    def __init__(self, size=0):
        """Initializes square"""
        self.__size = size

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter
        Args:
            value: size must be an integer, size must be >= 0
        """
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

    def my_print(self):
        """prints the square with # in stdout"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
