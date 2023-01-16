#!/usr/bin/python3
def no_c(my_string):
    while "C, c" in my_string:
        my_string.remove("C", "c")
    return my_string
