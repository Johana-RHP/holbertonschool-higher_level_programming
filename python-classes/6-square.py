#!/usr/bin/python3
"""Defines the class square the instance size and its area"""


class Square:
    """
    Define a square
    Args:
        size : size of a side in square
    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        area8self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        Setter
        Args:
            value: size must be an integer, size must be >= 0
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @property
    def position(self):
        """
        Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        """
        Setter
        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(new_position) is not tuple or len(new_position) != 2 or \
            type(new_position[0]) is not int or \
            type(new_position[1]) is not int or \
            new_position[0] < 0 or new_position[1] < 0:
                raise TypeError("position must be a tuple \
                        of 2 positive integers")
        else:
            self.__position = new_position

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
                print(' ' * self.position[0], end="")
                print("#" * self.size)
