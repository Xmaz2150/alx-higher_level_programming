#!/usr/bin/python3
""" defines Student class """


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns clean attributes of
            self """

        if attrs is None:
            return self.__dict__

        og_dict = self.__dict__
        new_dict_att = {}
        for key in attrs:
            new_val = og_dict.get(key)
            if new_val is not None:
                new_dict_att[key] = new_val
        return new_dict_att

    def reload_from_json(self, json):
        """  """

        for k, v in json.items():
            setattr(self, k, v)
