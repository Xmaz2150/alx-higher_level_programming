#!/usr/bin/python3
"""One class module"""


class Rectangle:
    """ Empty Recatangle class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __print__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                rect += '#'
                for j in range(self.__width - 1):
                    rect += '#'
                if i != self.__height - 1:
                    rect += '\n'
            return rect

    def __str__(self):
        return self.__print__()