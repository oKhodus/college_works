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

    def remove_dups(self):
        """Removes duplicates from sorted linked list"""
        # starts from head
        current = self.head
        # going through if at least two nodes 
        while current and current.next:
            # skip the next node if dupl
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                # moving to next node
                current = current.next

    def display(self):
        """Print the values of all nodes in the linked list"""
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print(None)

ll = LinkedList()

for elem in range(1, 6):
    ll.insert_at_head(elem)
    ll.insert_at_head(elem)
# if accidentally was added elements twice
ll.display()
# 5->5->4->4->3->3->2->2->1->1->None (before removing)
ll.remove_dups()
ll.display()
# 5->4->3->2->1->None (after removing)
