#!/usr/bin/python3
"""
function that returns True if its inherited from a class
"""


def inherits_from(obj, a_class):
    """
    checks the object
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
