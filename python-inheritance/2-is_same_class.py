#!/usr/bin/python3
"""
function that returns true if the object is
exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """returns true if instance"""
    return type(obj) is a_class
