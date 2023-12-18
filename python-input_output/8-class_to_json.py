#!/usr/bin/python3
"""Module with class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    obj_dict = obj.__dict__.copy()

    for key, value in obj_dict.items():
        if hasattr(value, '__dict__'):
            obj_dict[key] = class_to_json(value)
    return obj_dict
