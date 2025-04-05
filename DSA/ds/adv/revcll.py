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

    def reverse(self):
        """Reverses a circular linked list"""
        # if ls is empty or contains only one node - no need to reverse
        if self.head is None or self.head.next is self.head:
            return

        prev = None
        # starts from the head
        current = self.head
        # temporary var to store the next node
        next_node = None
        # iterating through the ls until reach head again
        while current.next != self.head:
            # store next node before modifying pointer
            next_node = current.next
            # reverse link and make current point to prev node
            current.next = prev
            # move prev forward to current node
            prev = current
            # move current forward to next node
            current = next_node

            # if reach basic head - break
            if current == self.head:
                break
        # reverse link for the last node
        current.next = prev
        # make prev head point to new head to save cll structure
        self.head.next = current
        # refresh head to new first node
        self.head = current

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



for elem in range(1, 6):
    cl.insert_at_head(elem)

cl.display()

for elem in range(2, 6):
    cl.insert_at_tail(elem)

cl.display()

for elem in range(1, 6):
    if elem % 2 == 0:
        cl.delete(elem)
        cl.delete(elem)

cl.display()

cl.insert_at_head(500)
# cl.reverse()
cl.display()

cl.reverse()
cl.display()