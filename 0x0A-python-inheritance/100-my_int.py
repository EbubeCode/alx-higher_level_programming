#!/usr/bin/python3
"""Module for class MyInt"""


class MyInt(int):
    """Reverses functionality of equals"""

    def __eq__(self, value):
        """reverse super's funtionality"""
        return super().__ne__(value)

    def __ne__(self, value):
        """reverse super's funtionality"""
        return super().__eq__(value)
