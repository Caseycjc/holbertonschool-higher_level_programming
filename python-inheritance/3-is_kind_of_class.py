#!/usr/bin/python3
"""
function that checks if an object is of or
inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """checks the object"""
    return type(obj) is a_class
