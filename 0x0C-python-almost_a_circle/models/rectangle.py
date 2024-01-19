#!/usr/bin/python3
""" Base subclass """
from models.base import Base


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize instance """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if id is not None:
            self.id = id
        else:
            self.inc_obj_no(1)
            self.id = self.get_obj_no()

    @property
    def width(self)
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self)
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value)
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value)
        """ y setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self)
        """ area of rect """
        return self.width * self.height

    def display(self):
        """ visual repr of rect """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ str repr of class """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -  {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ instance updator """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, ["id", "width", "height", "x", "y"][i], arg)
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if v is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ to dictionary """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
