#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and then saves them to a file.
"""

import sys
from os.path import exists
from json import load, dump
from pathlib import Path
from importlib import import_module


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as file:
        dump(my_obj, file)


def load_from_json_file(filename):
    """Creates an Object from a "JSON file"."""
    with open(filename, mode='r', encoding='utf-8') as file:
        return load(file)
