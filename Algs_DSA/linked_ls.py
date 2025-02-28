class Node:
    """_summary_
    """
    def __init__(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.value = value
        self.next = None

class LinkedList:
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        self.head = None

    def insert_at_head(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """_summary_

        Args:
            value (_type_): _description_
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
        """_summary_

        Args:
            value (_type_): _description_
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
        """_summary_
        """
        current_node = self.head
        # print("head:")
        while current_node != None:
            print(current_node.value, end="|")
            current_node = current_node.next
        # print(f"tail:", None)

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