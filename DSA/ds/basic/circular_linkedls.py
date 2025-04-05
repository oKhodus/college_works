from typing import Any


class Node:
    """A class creating a node in a circular linked list"""

    def __init__(self, value: Any):
        """Initialize a new node with a given value

        Args:
            value (Any): The value which will be added to the list
        Note:
            - "self.next" (Any): Next node of the cll (kind of flag)
        """
        self.value: Any = value
        self.next: Any = None

    def __repr__(self):
        """
        repr - nodes and values for checking is correct or not
        """
        return f"Value: {self.value} Next: {self.next.value}"


class CircularLinkedList:
    """A class representing a circular linked list"""

    def __init__(self):
        """Making empty circular linked list"""
        self.head = None

    def insert_at_head(self, value) -> None:
        """Insert a new node with the given value at the HEAD of the list

        Args:
            value (Any): The value which will be inserted
        """
        new_node = Node(value)
        # if cll empty
        if self.head is None:
            # new node which has a link on itself (making circular)
            new_node.next = new_node
            # head now has a link to a new node
            self.head = new_node
            return

        # impl of current for going through cll
        current = self.head
        # seeking od last node
        while current.next != self.head:
            current = current.next

        # new node has a link on 'old' head
        new_node.next = self.head
        # last node has a link on new node
        current.next = new_node
        # refreshing of HEAD to the new node
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node with the given value at the TAIL of the list

        Args:
            value (Any): The value which will be inserted
        """
        new_node = Node(value)
        # if cll empty
        if self.head is None:
            # new node which has a link on itself (making circular)
            new_node.next = new_node
            # head now has a link to a new node
            self.head = new_node
            return

        # impl of current for going through cll
        current = self.head
        # seeking od last node
        while current.next != self.head:
            current = current.next

        # last node has a link on new node
        current.next = new_node
        # new node has a link on 'old' head
        new_node.next = self.head

    def delete(self, value):
        """Delete the first occurrence of a NODE with the given value

        Args:
            value (Any): The value of the node to be deleted
        """
        # if list is already empty
        if self.head is None:
            return
        # if delete the head node
        if self.head.value == value:
            # if list has only one node
            if self.head.next == self.head:
                # now list is empty -> None
                self.head = None
                return

            # impl of current for going through cll
            current = self.head
            # seeking od last node
            while current.next != self.head:
                current = current.next
            # last node now has a link on the next after HEAD
            current.next = self.head.next
            # refreshing of HEAD
            self.head = self.head.next
            return

        # impl of current for going through cll
        current = self.head
        # seeking node which has a link to another node
        # (which will be deleted)
        while current.next != self.head:
            if current.next.value == value:
                # skipping node which will be deleted
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """Print the values of all nodes in the circlular linked list"""
        # if empty list
        if self.head is None:
            return
        # impl of current for going through cll
        current_node = self.head

        while True:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break

        print("back to head\n")


"""checking repr"""
# while current_node != None:
#     print(current_node)
#     current_node = current_node.next
#     if current_node == self.head:
#         print("back to head\n")
#         break


cl = CircularLinkedList()

cl.insert_at_head(3)
cl.insert_at_head(2)
cl.insert_at_head(1)

cl.display()
"""Output: 1 -> 2 -> 3 -> back to head"""
cl.insert_at_tail(4)
cl.insert_at_tail(5)

cl.display()
"""Output: 1 -> 2 -> 3 -> 4 -> 5 -> back to head"""
cl.delete(3)
cl.delete(1)

cl.display()
"""Output: 2 -> 4 -> 5 -> back to head"""
