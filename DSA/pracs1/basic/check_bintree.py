from re import match
from typing import Any, Type


class Stack:
    def __init__(self):
        """Stack implementation using a list"""
        # make ls to store stack elems
        self.stack = []

    def push(self, item):
        """Add an element to the top of the stack

        Args:
            item (Any): data which will be appended
        """
        self.stack.append(item)

    def pop(self):
        """Remove and return the top element

        Returns:
            element: from stack
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        """Return the top element without removing it

        Returns:
            element: from stack
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.stack) == 0

    def display(self, message: str = None):
        """Print the stack with an optional message

        Args:
            message (str, optional): String which will be printed. Defaults to None.
        """
        print((f"{message}: " if message else "") + f"{self.stack}")


class BinaryNode:
    def __init__(
        self, BinaryNode_id: int, data: Any, parent: Type["BinaryNode"] = None
    ) -> None:
        """BinaryNode class representing a node in a binary tree

        Args:
            BinaryNode_id (int): Unique identifier for the node
            data (Any): Data stored in the node
            parent (Type[&quot;BinaryNode&quot;], optional): Reference to the parent node. Defaults to None.
        """
        self.id = BinaryNode_id
        self.data = data
        self.parent = parent
        # init the left child node
        self.left = None
        # init the right child node
        self.right = None

    def __repr__(self) -> str:
        """String representation of the node"""
        return f"bN{self.id}({self.data})"


class BinaryTree:
    def __init__(self, root_data: Any) -> None:
        """BinaryTree class representing a binary tree structure

        Args:
            root_data (Any): init root data
        """
        # make root node with id 0
        self.root = BinaryNode(0, root_data)
        # dict to store nodes by id
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node_id: int = 0) -> BinaryNode:
        """Adds a child node to a given parent node in the tree

        Args:
            child_data (Any): The data for the child node
            to_node_id (int, optional): The ID of the parent node. Defaults to 0

        Raises:
            Exception: Raise an error if the parent already has two children

        Returns:
            Node: The newly created child node
        """
        # find the parent node by id
        parent = self.map[to_node_id]
        # make a new unique id for the child node
        last_id = len(self.map)
        new_node = BinaryNode(last_id, child_data, parent)
        # make the new node as the left child if empty
        if not parent.left:
            parent.left = new_node
        # make the new node as the right child if empty
        elif not parent.right:
            parent.right = new_node
        else:
            raise Exception(
                "In BinaryTree one can't be added more than 2 Nodes to parent"
            )
        # store the new node in the map
        self.map[last_id] = new_node

    def __iter__(self):
        stack = Stack()
        # start friom the root node
        stack.push(self.root)

        while not stack.is_empty():
            # get the top node
            current: BinaryNode = stack.pop()
            if current.left:
                # push left child in stack
                stack.push(current.left)
            if current.right:
                # push right child in stack
                stack.push(current.right)
            yield current

    def is_full(self) -> bool:
        """Check if the binary tree is full (all nodes have 0 or 2 children)

        Returns:
            bool: False if a node has only one child, else -> True
        """
        for node in self:
            if node.left and not node.right:
                # if tree isn't full
                return False
            # continue checking
            return True


if __name__ == "__main__":
    tree = BinaryTree(1)
    line_num = int(input())

    for _ in range(line_num):
        line = input()
        res = match(r"(?P<parent_id>\d+): (?P<left>\d+)? ?(?P<right>\d+)?\s*", line)

        if res["left"]:
            tree.add_child(int(res["left"]), int(res["parent_id"]))
        if res["right"]:
            tree.add_child(int(res["right"]), int(res["parent_id"]))

    print(tree.is_full())

"""
examples:
1)

3
|||
0: 1 2
1: 3 4
2: 5
|||
-> True

2)

2
|||
0: 1
1: 2 3
|||
-> False
# because node 0 has only 1 child
"""