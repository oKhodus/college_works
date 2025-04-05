from typing import Any, Type

class Stack:
    """Stack implementation"""
    def __init__(self):
        # make list to store stack elems
        self.stack = []

    def push(self, item):
        # add an elem to the top of the stack
        self.stack.append(item)

    def pop(self):
        # rm and return the top elem
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        # return the top elem without rming it
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self, message: str = None):
        print(
            (f"{message}: " if message else "") +
            f"{self.stack}"
        )


class Node:
    """Node class representing a tree node"""
    def __init__(self, node_id: int, data: Any, parent: Type['Node'] = None) -> None:
        """Initializing of tree node

        Args:
            node_id (int): unique id for the node
            data (Any): data stored in the node
            parent (Type[&#39;Node&#39;], optional): Reference to the parent node. Defaults to None.
        """
        self.id = node_id
        self.data = data
        self.parent = parent
        self.child = []

    def __repr__(self) -> str:
        """String representation of the node"""
        return f"N{self.id}({self.data})"


class Tree:
    def __init__(self, root_data: Any) -> None:
        """Tree class representing a tree structure

        Args:
            root_data (Any): Create root node with ID 0
        """
        self.root = Node(0, root_data)
        # dict to store nodes by id
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node_id: int = 0) -> Node:
        """Adds a child node to a given parent node in the tree

        Args:
            child_data (Any): The data for the child node
            to_node_id (int, optional): The ID of the parent node. Defaults to 0

        Returns:
            Node: The newly created child node
        """
        # find the parent node by id
        parent = self.map[to_node_id]
        # generate a new unique id for the child node
        last_id = len(self.map)
        # Create a new node
        new_node = Node(last_id, child_data, parent)
        # Add the new node to the parent's child list
        parent.child.append(new_node)
        # Store the new node in the map
        self.map[last_id] = new_node
        return new_node

    def __iter__(self):
        """Iterator for traversing the tree using Depth-First Search"""
        stack = Stack()
        # Start from the root node
        stack.push(self.root)

        while not stack.is_empty():
            # get the top node
            current: Node = stack.pop()
            for child in current.child:
                # push all children in the stack
                stack.push(child)
            yield current
            
    def degree(self, node_id: int) -> int:
        """Returns the number of children (degree) of a given node

        Args:
            node_id (int): The id of the node

        Returns:
            int: The number of children of the specified node
        """
        # find the node by id
        node = self.map[node_id]
        # return the num of children
        return len(node.child)


if __name__ == "__main__":
    tree = Tree('A')
    B = tree.add_child('B')  
    C = tree.add_child('C')
    tree.add_child('D', B.id)
    tree.add_child('E', B.id)
    tree.add_child('F', B.id)
    G = tree.add_child('G', C.id)
    H = tree.add_child('H', G.id)
    
    node_id = int(input())
    print(tree.degree(node_id))

