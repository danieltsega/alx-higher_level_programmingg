#!/usr/bin/python3
"""Defining a Node Class"""


class Node:
    """A Class that defines a Node
    """

    def __init__(self, data, next_node=None):
        """A method that initializes arguments
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """A method that gets a data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """A method that sets a value to the data
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """A method that gets the next node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """A method that sets a value to the next node
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defining a Singlinked Class"""


class SinglyLinkedList:
    """A clsaa that defines a singly linked list
    """

    def __str__(self):
        """A str method
        """

        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """A method that initializes the list
        """

        self.__head = None

    def sorted_insert(self, value):
        """A method that sorts a value to list
        """

        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
