#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square.
"""


class Square:
    """Creates A Square"""
    def __init__(self, size=0):
        """Initializes Square"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
