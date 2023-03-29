#!/usr/bin/python3

"""This module defines a simply linked list."""


class Node:
    """The node class of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize the node with it's integer data
        and next node if exists.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the private data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the private data, has to be int."""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter for the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node."""
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class defines a singly linked list with inserting only."""

    def __init__(self):
        """Initialization with a head is None."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting in a linked list in a sorted order."""
        if self.__head is None:
            self.__head = Node(value, None)
            return

        new = Node(value, None)
        n = self.__head
        if value <= n.data:
            new.next_node = n
            self.__head = new
            return

        while (n.next_node and value > n.next_node.data):
            n = n.next_node
        new.next_node = n.next_node
        n.next_node = new

    def __str__(self):
        """Printing the linked list."""
        list_str = ""
        n = self.__head
        while n is not None:
            list_str += f"{n.data}"
            n = n.next_node
            if n:
                list_str += "\n"

        return list_str
