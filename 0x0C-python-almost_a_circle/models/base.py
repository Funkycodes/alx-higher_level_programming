#!/usr/bin/python3
"""Module contains Base Class

Defines id attribute for subclasses

"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a json representation of instance

        Args:
            list_dictionaries (dict): Dictionary form of object

        Returns:
            _type_: _description_
        """
        if list_dictionaries is None:
            list_dictionaries = []
        json_rep = json.dumps(list_dictionaries)
        return json_rep

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(cls.to_dictionary(obj))
        json_str = cls.to_json_string(obj_list)
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        class_name = cls.__name__
        if class_name == "Rectangle":
            dummy = cls(1, 1)
        elif class_name == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        obj_list = []
        with open(filename, 'r') as f:
            json_string = f.read()
            list_rep = cls.from_json_string(json_string)
            for li in list_rep:
                obj_list.append(cls.create(**li))
        return obj_list
