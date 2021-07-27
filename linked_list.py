class Node():
    """
    Implementation of a node within a linked list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """
    head = None

    def __init_(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """ 
        returns number of nodes in list
        takes linear time
        """

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new node containing data at list head
        takes constant time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search and return first node containing data matching key
        Else return None

        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts new node at given index containing given data#
        Insertion takes O(1) 
        but finding the nodes position takes O(n)

        Takes overall O(n)
        """

        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes the Node with the given key data
        Returns the Node or None if not found
        Takes O(n)
        """
        current = self.head
        found = False
        if current.data == key:
            self.head = current.next_node
            found = True
        last_node = None
        while current and not found:
            if current.data == key:
                last_node.next_node = current.next_node
                found = True
            else:
                last_node = current
                current = current.next_node
        return current

    def remove_index(self, index):
        """
        Removes Node at given index
        Returns removed node 
        Takes O(n)
        """

        current = self.head
        if index == 0:
            self.head = current.next_node
            return current
        if index > 0:
            position = index
            prev_node = None

            # get previous node
            while position >= 1:
                prev_node = current
                current = current.next_node
                position -= 1

            prev_node.next_node = current.next_node
            return current

    def node_at_index(self, index):
        """
        Returns the node at given index

        Takes O(n)
        """
        if index == 0:
            return self.head
        if index > 0:
            current = self.head
            while index > 0:
                current = current.next_node
                index -= 1
            return current

    def __repr__(self):
        """
        Returns string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)
