#!/usr/bin/python3
"""Module that returns True if the object
is exactly an instance of a class"""



def is_same_class(obj, a_class):
    """ function that returns true of false
depending on the object"""

    return type(obj) is a_class
