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
    indented_text = ""
    for char in text:
        indented_text += char
        if char in ".?:":
            indented_text += "\n\n"
    print(indented_text.strip())
