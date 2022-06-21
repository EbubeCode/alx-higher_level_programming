#!/usr/bin/python3
"""This module defines the Node class for a singly
linked list and the singly linked list class"""


class Node:
    """Holds the data of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for __data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for __data attribute"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for __next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for __next_node attribute"""
        if type(value) == type(self) or not value:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Implementation for a singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """prints the entire list in stdout"""
        strn = ''
        head = self.__head
        while head:
            strn += str(head.data)
            head = head.next_node
            if head:
                strn += '\n'
        return strn

    def sorted_insert(self, value):
        head = self.__head
        if head:
            prev = None
            while head:
                if value < head.data:
                    current = Node(value, head)
                    if prev:
                        prev.next_node = current
                    else:
                        self.__head = current
                    return
                else:
                    prev = head
                    head = head.next_node
            current = Node(value)
            prev.next_node = current
        else:
            head = Node(value)
            self.__head = head
