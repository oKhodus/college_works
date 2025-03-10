class Node:
    """A class creating a node in a circular linked list"""

    def __init__(self, value):
        """Initialize a new node with a given value

        Args:
            value (Any): The value which will be added to the list
        """
        self.value = value
        self.next = None

    def __repr__(self):
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

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node with the given value at the TAIL of the list

        Args:
            value (Any): The value which will be inserted
        """
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
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
            if self.head.next == self.head:
                self.head = None
                return

            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next
            return

        current = self.head

        while current.next != self.head:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """Print the values of all nodes in the circlular linked list"""
        # if empty list
        if self.head is None:
            return

        current_node = self.head

        while current_node != None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break

        print("back to head\n")
# checking repr
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

cl.insert_at_tail(4)
cl.insert_at_tail(5)

cl.display()

cl.delete(3)
cl.delete(1)

cl.display()