class Node:
    """A class creating a node in a linked list."""
    def __init__(self, value):
        """Initialize a new node with a given value

        Args:
            value (int, float, str and etc.): _description_
        """
        self.value = value
        self.next = None

class LinkedList:
    """A class representing a singly linked list"""
    def __init__(self):
        """Initialize an empty linked list with --head--"""
        self.head = None

    def insert_at_head(self, value):
        """Insert a new node with the given value at the HEAD of the list

        Args:
            value (int, float, str and etc.): The value which will be inserted
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node with the given value at the TAIL of the list

        Args:
            value (int, float, str and etc.): The value which will be inserted
        """
        new_node = Node(value)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        
    def delete(self, value):
        """Delete the first occurrence of a NODE with the given value

        Args:
            value (int, float, str and etc.): The value of the node to be deleted
        """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next != None and current.next.value != value:
            current = current.next
        
        if current.next != None:
            current.next = current.next.next

    def display(self):
        """Print the values of all nodes in the linked list"""
        current_node = self.head
        # print("head:")
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print(None)

ll = LinkedList()

ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(1)

ll.insert_at_tail(4)
ll.insert_at_tail(5)
ll.insert_at_tail(6)

ll.delete(1)
ll.delete(3)
ll.delete(5)

ll.display()
#--- 2|4|6|