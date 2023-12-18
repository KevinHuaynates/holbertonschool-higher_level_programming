#!/usr/bin/python3
"""Module defining the MyList class."""

class MyList(list):
    """Inherits from list and adds a print_sorted method."""
     def print_sorted(self):
         """Prints the list sorted in ascending order."""
         print(sorted(self))
