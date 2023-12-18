#!/usr/bin/python3
"""
Module documentation goes here.
"""


class BaseGeometry:
    """BaseGeometry class definition"""
    def area(self):
        """Public instance method to raise an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method to validate the integer value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
