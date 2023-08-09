#!/usr/bin/python3
"""
This module contains the class Base
"""
import json
import os.path


class Base:
    """
    This class is the “base” of all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id and set as id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return = "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string
        representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)

        result = []
        if list_objs is None:
            pass
        else:
            for objs in range(len(list_objs)):
                result.append(list_objs[i].to_dictionary())

        with open(filename, "w") as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ list of dictionaries to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            uwu = cls(6)
        elif cls.__name__ == "Rectangle":
            uwu = cls(6, 6)
        uwu.update(**dictionary)
        return uwu

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for i in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[i]))
        return list_ins
