#!/usr/bin/python3
"""Rectangle module.
This module contains a class that defines a rectangle.
"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (0 > value):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (0 > value):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if (self.width is 0 or self.height is 0):
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        if (self.width is 0 or self.height is 0):
            return ""
        rekt = "#" * self.width + "\n"
        rekt = rekt * self.height
        rekt = rekt[:-1]
        return (rekt)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
