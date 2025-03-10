class Node:
    def __init__(self, value):
        """Initialize node with value

        Args:
            value (Any): value which will be inserted into list
        """
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return str which represents the node - which will show prev and next values"""
        prev_val = self.prev.value if self.prev else "None"
        next_val = self.next.value if self.next else "None"
        return f"Prev: {prev_val} Value: {self.value} Next: {next_val}"

class Dll:
    def __init__(self):
        """Initialize Double linked list (example: 1 <-> 2 <-> 3)"""
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """Insert a node at the head of the list

        Args:
            value (Any): value which will be inserted at the head
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_tail(self, value):
        """Insert a node at the tail of the list

        Args:
            value (Any): value which will be inserted at the tail
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


    def delete(self, value):
        """Delete the first occurrence of a node with the given value."""
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        current = self.head
        while current and current.value != value:
            current = current.next

        if current:
            if current.next:
                current.next.prev = current.prev
            else:
                self.tail = current.prev

            if current.prev:
                current.prev.next = current.next

    def display_forward(self):
        """Display the list from head to tail"""
        current_node = self.head

        while current_node:
            print(current_node.value, end=" <-> " if current_node.next else "\n")
            current_node = current_node.next

    def display_backward(self):
        """Display list from tail to head"""
        current_node = self.tail

        while current_node:
            print(current_node.value, end=" <-> " if current_node.prev else "\n")
            current_node = current_node.prev


dll = Dll()
dll.insert_head(3)
dll.insert_head(2)
dll.insert_head(1)
dll.insert_tail(4)

dll.display_forward()
dll.display_backward()

dll.delete(2)
dll.display_forward()
dll.display_backward()