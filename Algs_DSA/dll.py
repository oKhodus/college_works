class Node:
    def __init__(self, value):
        """_summary_

        Args:
            value (Any): value which will be inserted into list
        """
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        prev_val = self.prev.value if self.prev else "None"
        next_val = self.next.value if self.next else "None"
        return f"Prev: {prev_val} Value: {self.value} Next: {next_val}"

class Dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_tail(self, value):
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
        current_node = self.head

        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.next
        print(None)

    def display_backward(self):
        current_node = self.tail

        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.prev
        print(None)

        # while current_node:
        #     print(current_node)
        #     current_node = current_node.prev
        # print(None)


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