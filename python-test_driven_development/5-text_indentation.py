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

    current_line = ""

    for char in text:
        if char in ".?:":
            print(current_line.strip() + "\n\n", end="")
            current_line = ""
        else:
            current_line += char
        if current_line:
            print(current_line.strip())
