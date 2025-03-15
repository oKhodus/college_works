from typing import Any


class Node:
    """Creating of a node in dll"""

    def __init__(self, value: Any):
        """Initialize node with value

        Args:
            value (Any): value which will be inserted into list
        """
        self.value: Any = value
        self.next: Any = None
        self.prev: Any = None

    def __repr__(self):
        """Return str which represents the node - which will show prev and next values"""
        prev_val = self.prev.value if self.prev else "None"
        next_val = self.next.value if self.next else "None"
        return f"Prev: {prev_val} Value: {self.value} Next: {next_val}"


class Dll:
    """Making Dll"""

    def __init__(self):
        """Initialize Double linked list (example: 1 <-> 2 <-> 3)"""
        # the first node
        self.head = None
        # the last node
        self.tail = None

    def insert_head(self, value):
        """Insert a node at the head of the list

        Args:
            value (Any): value which will be inserted at the head
        """
        new_node = Node(value)
        # if ls is emty
        if self.head is None:
            # set both to the new node
            self.head = new_node
            self.tail = new_node
            return
        # next node has a link to the current head
        new_node.next = self.head
        """
        The current head was the first element,
        but now I'm insert a new node before it
        """
        self.head.prev = new_node
        # updating head to the new node
        self.head = new_node

    def insert_tail(self, value):
        """Insert a node at the tail of the list

        Args:
            value (Any): value which will be inserted at the tail
        """
        new_node = Node(value)
        #  if ls is empty
        if self.head is None:
            # set both to the new node
            self.head = new_node
            self.tail = new_node
            return
        # current tail will point to the new node
        self.tail.next = new_node
        # new node will point back to the current tail
        new_node.prev = self.tail
        # refresh tail to the new node
        self.tail = new_node

    def delete(self, value):
        """Delete the first occurrence of a node with the given value.

        Args:
            value (Any): The value of the node to be deleted
        """

        # if ls is emty, stop func
        if self.head is None:
            return

        # if node which will be deleted is the head
        if self.head.value == value:
            # move forward to the next node
            self.head = self.head.next
            # if there is a new head
            # (after rm Head, new head will second, if it exists)
            if self.head:
                # set the prev pointer of the new head to NOne -
                # because no node before it
                self.head.prev = None
            else:
                # if ls is now empty - refresh tail to NONE
                self.tail = None
            return

        current = self.head
        # going through the ls to find the node, which will be deleted
        while current and current.value != value:
            current = current.next

        # if the node was found
        if current:
            # if node isn't the last node
            if current.next:
                # refresh next node's prev pointer
                current.next.prev = current.prev
            else:
                # if it's the last node - refresh tail
                self.tail = current.prev

            # if node isn't the first
            if current.prev:
                # refresh prev node's next pointer
                current.prev.next = current.next

    def display_forward(self):
        """Display the list from head to tail"""
        current_node = self.head

        while current_node:
            print(current_node.value, end=" ⇄ " if current_node.next else "\n")
            current_node = current_node.next

    def display_backward(self):
        """Display list from tail to head"""
        current_node = self.tail

        while current_node:
            print(current_node.value, end=" ⇄ " if current_node.prev else "\n")
            current_node = current_node.prev


dll = Dll()
dll.insert_head(3)
dll.insert_head(2)
dll.insert_head(1)
dll.insert_tail(4)
"""Output: 1 ⇄ 2 ⇄ 3 ⇄ 4"""
dll.display_forward()
dll.display_backward()
"""Output: 4 ⇄ 3 ⇄ 2 ⇄ 1"""
dll.delete(2)
dll.display_forward()
"""Output: 1 ⇄ 3 ⇄ 4"""
dll.display_backward()
"""Output: 4 ⇄ 3 ⇄ 1"""
