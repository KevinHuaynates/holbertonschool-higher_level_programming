#!/usr/bin/python3
"""
Module: text_indentation
Description: This module provides a simple Python script.
"""

def text_indentation(text):
    """Function: atext_indentation(text)"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = " "
    for char in text:
        buffer += char
        if char in ['.', '?', ':']:
            print(buffer.strip()+" ")
            buffer = " "

    if buffer:
        print(buffer.strip())

if __name__ == "__main__":
    text_indentation("Holberton School")
