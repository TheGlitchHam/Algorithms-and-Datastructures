class Node:
    """
    An Object for storing a single node of a linked list.

    Models two attributes:
        data: The Values it stores
        next_node: Reference to the next node in the list

    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __str__(self) -> str:
        print("Data: ", self.data, " || Next Node: ", self.next_node)

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list implementation
    """

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self) -> int:
        """
        Returns number of nodes in the list
        Takes O(n) time
        Traverses the whole list
        """
        current = self.head
        counter = 0

        while current:
            counter += 1
            current = current.next_node

        return counter
