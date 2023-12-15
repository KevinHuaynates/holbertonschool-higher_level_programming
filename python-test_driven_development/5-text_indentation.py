#!/usr/bin/python3
"""
This module contains a function to print a text
with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':' characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in '.?:':
            print('\n\n', end='')
        else:
            print(char, end='')
