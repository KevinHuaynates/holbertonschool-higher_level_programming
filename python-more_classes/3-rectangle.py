#!/usr/bin/python3
"""Class Rectangle that defines a rectangle"""


class rectangle
"""Defines a rectangle with private width and height attributes"""


    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.heght = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public method to calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Public method to calculate and return the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
