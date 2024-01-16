#!/usr/bin/python3
""" Class module """


class Base:
    """ base class for all future classes """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.inc_obj_no(1)
            self.id = self.get_obj_no()

    @classmethod
    def get_obj_no(cls):
        return cls.__nb_objects

    @classmethod
    def inc_obj_no(cls, n):
        cls.__nb_objects += n
