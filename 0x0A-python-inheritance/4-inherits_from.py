#!/usr/bin/python3
"""
module with method inherits_from
"""


def inherits_from(obj, a_class):
    """Returns true if the object is inherited from a specified class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
