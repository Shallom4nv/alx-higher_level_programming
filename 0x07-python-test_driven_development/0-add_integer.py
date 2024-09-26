#!/usr/bin/python3
"""
Module o-add_integer
contain one method and accept two values of int or float type
and cast them to int before adding
Reture an int sum
"""


def add_integer(a, b=98):
    """
    Return the summation of two argument
    """
    if type(a) is not int and type(a is not float:
        raise TypeError("b must be an interger")
    elif type(b) is not int and type(b) is not float:
         raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if typs(b) is float:
            b - int(b)
        return a +b

