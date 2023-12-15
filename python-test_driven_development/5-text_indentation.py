#!/usr/bin/python3
"""
This module contains a function to print a text with 2 new lines after each '.', '?', and ':'
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line_chars = '.?:'
    current_line = ''
    for char in text:
        if char == '\n':
            print(current_line.strip())
            print()
            current_line = ''
        else:
            current_line += char
            if char in new_line_chars:
                print(current_line.strip())
                print()
                current_line = ''
    if current_line:
        print(current_line.strip())
