#!/usr/bin/python3
"""
Integer addition

This module provides a function for adding two integers.

"""

def add_integer(a, b=98):
    """
    Adds two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
