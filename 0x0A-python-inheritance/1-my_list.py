#!/usr/bin/python3
"""
Module for the class MyList
"""


class MyList(list):
    """
    A custome list class that defines the method
    print_sorted
    """

    def print_sorted(self):
        """
        This method prints the elements in the list
        in sorted order
        """
        print(sorted(self))
