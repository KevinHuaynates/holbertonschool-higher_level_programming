#!/usr/bin/python3
"""
Module 1-my_list

A module that defines the MyList class.
"""


class MyList(list):
    """
    A class that inherits from list and adds a method to print sorted list.
    """

    def print_sorted(self):
        """
        Public instance method to print the list in sorted order.

        Args:
            self: The object instance.

        Returns:
            None.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Uncomment the following lines for testing using the provided test file
# if __name__ == "__main__":
#     my_list = MyList()
#     my_list.append(1)
#     my_list.append(4)
#     my_list.append(2)
#     my_list.append(3)
#     my_list.append(5)
#     print(my_list)
#     my_list.print_sorted()
#     print(my_list)
