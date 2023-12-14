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
        __init__ Method - Initializes a new instance of the Square class.
        """
        self.size = size

    @property
    def size(self):
        """
        size Getter Method - Retrieves the value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size Setter Method - Sets the value of the size attribute.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area Method - Computes the area of the square.
        """
        return self.__size ** 2
