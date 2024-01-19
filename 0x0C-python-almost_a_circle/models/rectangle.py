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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -  {self.width}/{self.height}"

    def update(self, *args, **kwargs):
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
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
