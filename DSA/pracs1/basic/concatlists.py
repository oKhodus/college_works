class Node:
    def __init__(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.value = value
        self.next = None

class LinkedList:
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
            """Insert a new node with the given value at the TAIL of the list

            Args:
                value (int, float, str and etc.): The value which will be inserted
            """
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
                return

            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def display(self):
        """_summary_
        """
        current = self.head
        while current != None:
            print(
                current.value, end="->" if current.next else "\n"
            )
            current = current.next
    
    def concatenate(self, another_list):
        """_summary_

        Args:
            another_list (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.head is None:
            return another_list
        if another_list.head is None:
            return self

        current = self.head
        while current.next != None:
            current = current.next
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
ll2.display()

conc_ll = ll1.concatenate(ll2)

conc_ll.display()
