#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a + (0, 0)
    b1, b2 = tuple_b + (0, 0)
    return (a1 + b1, a2 + b2)
if __name__ == "__main__":
    add_tuple = __import__('7-add_tuple').add_tuple
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
