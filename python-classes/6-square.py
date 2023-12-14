#!/usr/bin/python3
"""This module defines a Square class with position handling."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Sets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(n, int) for n in value) or not all(n >= 0 for n in value))
        raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters and position."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
