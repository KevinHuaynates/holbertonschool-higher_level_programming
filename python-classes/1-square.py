#!/usr/bin/python3

class Square:
    """
    Esta es una clase Square que define un cuadrado.
    Attributes:
    __size (int): El tamaño del cuadrado.
    
    """
    def __init__(self, size):
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)
