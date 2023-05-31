#!/usr/bin/python3
"""
This module provides a class MyList that inherits from list.
"""


class MyList(list):
    """
    A custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
