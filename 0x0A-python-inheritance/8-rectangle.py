#!/usr/bin/python3
BaseGeometry = __import__('base_geometry').BaseGeometry

"""
module with Rectangle class
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
