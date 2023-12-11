#!/usr/bin/paython3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
         """initializes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def validator(self, name, value):
        """validateor the input """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == 'width' or name == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """return area of rectangle"""
        return (int(self.width) * int(self.height))

    def display(self):
        """ print the rectangle """
        print('\n'*self.y, end="")
        for i in range(self.height):
            row = "".join(" " * self.x + "#" * self.width)
            print(row)

    def __str__(self):
        """ return rectangle """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width, self.height)

    def update(self, id=None, width=None, height=None, x=None, y=None):
        """ update the argument """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
