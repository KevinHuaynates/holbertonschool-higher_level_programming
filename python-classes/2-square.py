#!/usr/bin/python3
"""
Documentation Module - This module contains the definition of the Square class.
"""


class Square:
    """
    Square Class - Represents a square.
    """
    def __init__(self, size=0):
        """
        __init__ Method - Initializes a new instance of the Square class

        Args:
            size (int, optional): The size of the square. Default value is 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
