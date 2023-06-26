#!/usr/bin/python3
"""
This program define a Student in a class
"""


class Student:
    """Class of a student"""
    def __init__(self, first_name, last_name, age):
        """
        Args:
        first_name: str
        last_name: str
        age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            k = {}
            for a in attrs:
                if a in self.__dict__:
                    k[a] = self.__dict__[a]
            return k
        return self.__dict__

    def reload_from_json(self, json):
        for a in json:
            self.__dict__[a] = json[a]
