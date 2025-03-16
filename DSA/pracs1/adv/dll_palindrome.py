from typing import Any
# Replace classes with code you made on PS-1
# Replace ___ with your code

class Node:
    """Represents a node in dll (doubly linked list)"""

    def __init__(self, data):
        """Initializes a new node with given value

        Args:
            data (Any): The value stored in the node
        """
        self.data = data
        """
        next: A pointer to next node in list (default: None)
        prev: A pointer to previous node in list (default: None)
        """ 
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        """
        Implements dll with operations such as appending, displaying,
        and checking if the list represents a palindrome

        head: Points to the first node  
        tail: Points to the last node
        """
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Adds a new node with given data to end of the list
        """
        new_Node = Node(data)
        if not self.head:
            # if ls is empty - set head and tail to new node
            self.head = self.tail = new_Node
        else:
            # attach the new node in the end and refresh the tail pointer
            self.tail.next = new_Node
            new_Node.prev = self.tail
            # refresh tail to new node
            self.tail = new_Node


    def display(self):
        """
        Prints the elements of the list in order from head to tail
        """
        # starts from the head
        current = self.head
        while current != None:
            print(current.data, end=" ")
            # move to next
            current = current.next
        # \n
        print(
        
        )

    def is_palindrome(self):
        """Checks if ll represents a palindrome
        
        Returns:
            bool: True if ls is a polindrome else False

        Logic:
        - Use two pointers: `left` starts from head, `right` starts from tail
        - Compare `left.data` and `right.data`
        - Move `left` forward and `right` backward after each comparison
        - If all elems match in a symmetrical way - return True else - return False.
        """
        # initialize pointers
        left, right = self.head, self.tail
        while left and right and left != right and left.prev != right:
            # if vals don't match - it's not a polindrome
            if left.data != right.data:
                return False
            # moving left and right pointer forward ->
            left = left.next
            right = right.prev
        # if ends  - ls is a polindrome
        return True


linked_list = DoublyLinkedList()
list1 = list(map(int, input().split()))
for i in list1:
    linked_list.append(i)
print(linked_list.is_palindrome())

"""
For copying and checking

1 2 3 4 3 2 1
---> True

1 2 3 3 2 1
---> True

1 5 5 5 5 5
---> False
"""
