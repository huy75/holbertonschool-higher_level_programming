#!/usr/bin/python3
"""
This is module 100-singly_linked_list

It contains 2 classes: Node and SinglyLinkedList
"""


class Node:
    """
    defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Instantiates a Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter for private instance attribute data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        setter for private instance attribute data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        getter for private instance attribute next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for private instance attribute next_node
        """
        if not (type(value) == Node or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    defines a sinly linked list
    """
    def __init__(self):
        """
        instantiates a singly linked list
        """
        self.__head = None

    def __str__(self):
        """
        print a singly linked list
        """
        s = ""
        current = self.__head

        while current:
            s += str(current.data) + '\n'
            current = current.next_node
        return s[:-1]

    def sorted_insert(self, value):
        """
        inserts a new node in a singly linked list by increasing value
        """
        new = Node(value)
        current = self.__head
        if current is None:
            self.__head = new
            return

        if current.data > new.data:
            new.next_node = self.__head
            self.__head = new
            return

        while current.next_node and current.next_node.data <= new.data:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
        return
