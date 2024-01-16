#!/usr/bin/python3
""" Class module """


class Base:
    """ base class for all future classes """

    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            id = id
        else:
            self.__nb__objects += 1
            id = __nb__objects
