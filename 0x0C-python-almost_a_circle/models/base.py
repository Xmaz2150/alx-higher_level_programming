#!/usr/bin/python3
""" Class module """
import json


class Base:
    """ base class for all future classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init instance """
        if id is not None:
            self.id = id
        else:
            self.inc_obj_no(1)
            self.id = self.get_obj_no()

    @classmethod
    def get_obj_no(cls):
        """ instance no getter """
        return cls.__nb_objects

    @classmethod
    def inc_obj_no(cls, n):
        """ instance no setter """
        cls.__nb_objects += n

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json str"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves to file """
        filename = f"{cls.__name__}.json"

        data = []
        if list_objs is None:
            pass
        else:
            data = [obj.to_dictionary() for obj in list_objs]
        json_data = json.dumps(data)

        with open(filename, "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ obj from json """
        if not json_string:
            return []
        return json.loads(json_string)
