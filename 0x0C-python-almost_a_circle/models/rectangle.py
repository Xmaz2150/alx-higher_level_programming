#!/usr/bin/python3
""" Base subclass """
from models.base import Base


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if id is not None:
            self.id = id
        else:
            self.inc_obj_no(1)
            self.id = self.get_obj_no()
