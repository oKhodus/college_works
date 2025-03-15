from typing import Any


class Node:
    def __init__(self, value):
        """Initialize a new node with a given value

        Args:
            value (Any): _description_
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """Initialize an empty linked list"""
        self.head = None

    def insert_at_head(self, value):
        """Insert a new node with value at the head of the list

        Args:
            value (Any): The value which will be inserted at the head
        """
        new_node = Node(value)
        # make next new node point -> to the current head
        new_node.next = self.head
        # refresh head to the new node
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node with the given value at the TAIL of the list

        Args:
            value (Any): The value which will be inserted
        """
        new_node = Node(value)
        # if ls is empty - make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # going through until the tail
        current = self.head
        while current.next != None:
            current = current.next
        #  make current tail node point -> to the new node
        current.next = new_node

    def display(self):
        """Display the values of the nodes in the list"""
        current = self.head
        while current != None:
            print(current.value, end="->" if current.next else "\n")
            current = current.next

    def concatenate(self, another_list):
        """Concatenate another linked list to the current linked list

        Args:
            another_list (list): The linked list to be concatenated to the current list

        Returns:
            LinkedList: The refreshed list after concatenation
        """
        # if current ls is empty return another list
        if self.head is None:
            return another_list
        # # if another ls is empty return current list
        if another_list.head is None:
            return self

        # going through to the last node of the current list
        current = self.head
        while current.next != None:
            current = current.next
        # Link the last node of the current list to the head of another list
        current.next = another_list.head
        return self


ll1 = LinkedList()
ll2 = LinkedList()

ll1.insert_at_head(4)
ll1.insert_at_head(3)
ll1.insert_at_head(2)
ll1.insert_at_head(1)

ll2.insert_at_tail(7)
ll2.insert_at_tail(11)
ll2.insert_at_tail(18)
ll2.insert_at_tail(29)

ll1.display()
"""Output: 1->2->3->4"""
ll2.display()
"""Output: 7->11->18->29"""

conc_ll = ll1.concatenate(ll2)

conc_ll.display()
"""Output: 1->2->3->4->7->11->18->29"""
