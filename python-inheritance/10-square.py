#!/usr/bin/python3
"""
Module documentation goes here.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""
    def __init__(self, size):
        """Initializes a Square instance."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """String representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
