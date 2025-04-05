from typing import Any, Optional


class MaxChildrenError(Exception):
    """Raised when trying to add more than two children to a binary tree node."""
    pass


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


class AVLNode:
    """Represents a node in the AVL tree"""
    def __init__(self, AVLNode_id: int, data: Any, parent: 'AVLNode' = None):
        """Creates a new node in the AVL tree

        This method makes a new node in the AVL tree with the given data,
        sets its by unique id
        Sets the parent ppointer if provided. By default, both left and right children
        are set to 'None'
        And, the node's level in the AVL tree will be seeked:
        - The root node has a level of 0
        - Any other node's level is one more than its parent's level

        Args:
            AVLNode_id (int): The unique id of the node
            data (Any): The provided data stored in the node
            parent (AVLNode): The parent node of this node, 
            or 'None' if the node is the root of the AVL tree
        """
        self.id = AVLNode_id
        self.data = data
        self.parent = parent
        # left child
        self.left: Optional['AVLNode'] = None
        # right child
        self.right: Optional['AVLNode'] = None

        #  Calculation level of the node in the tree
        #  self.level = parent + 1 if parent else 0
        if parent:
            self.level = parent.level + 1
        else:
            self.level = 0

    def is_leaf(self) -> bool:
        """Checks is the node is leaf

        A node can be a leaf if it has no children (no left and no right)

        Returns:
            bool: True if the node is a leaf, else False 
        """
        return not (self.left or self.right)

    @property
    def height(self) -> int:
        """Calculates the height of the node

        The height of a leaf node is 0.
        For non-leaf nodes, the height is the maximum of the heights
        of the left and right children and plus 1

        Returns:
            int: The height of the node
        """
        if self.is_leaf():
            return 0

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return max(left_height, right_height) + 1

    def __repr__(self) -> str:
        """String representation of the AVL node"""
        return f"AVLNode id={self.id}, data={self.data}, height={self.height}"

    @property
    def balancing_factor(self) -> int:
        """Calculates the balancing factor of the node

        The balance factor is the difference between 
        the height of the left and right subtrees

        Returns:
            int: The balancing factor itself
        """
        # bf = Lh - Rh
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return left_height - right_height


class AVLTree:
    """Represents an AVL tree in a binary search tree"""
    def __init__(self, root_data: Any):
        """Initializes the AVL tree with the given root of the tree

        Makes the root of the AVL tree with the given value and assigns it 
        by a unique id of '0'
        Sets 'self.map' dictionary.
        The dictionary maps each node's id to the node itself (not just the value),
        making quick access to any node of tree

        Args:
            root_data (Any): The provided data is stored in the root
        """
        # make root node
        self.root = AVLNode(AVLNode_id=0, data=root_data)
        # dict to store nodes by id
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node: AVLNode | int) -> AVLNode:
        """Adds a child node to a parent node in the AVL tree

        Makes a new node with the given value and attaches it to the specified parent node
        The parent node is determined by its unique id or by providing the parent node object directly
        The child node is added to the left child or to the right child (if I can to add)
        If left and right children are full, an error will be raised

        Args:
            child_data (Any): The provided data that is stored in the node
            to_node (AVLNode | int): The parent node to attach the new child node to

        Returns:
            AVLNode: The newly created child node

        Raises:
            MaxChildrenError: If the parent node already has two children (left and right)
        """
        if isinstance(to_node, AVLNode):
            node_id = to_node.id
        else:
            node_id = to_node

        # get parent node from the map
        parent = self.map[node_id]
        # make a new unique id
        last_id = len(self.map)
        new_node = AVLNode(AVLNode_id=last_id, data=child_data, parent=parent)
        # attach by expressions
        if not parent.left:
            parent.left = new_node
        elif not parent.right:
            parent.right = new_node
        else:
            raise MaxChildrenError("In BinaryTree one can't be added more than 2 Nodes to parent")
        # store the new node in the map
        self.map[last_id] = new_node
        return new_node

    def __iter__(self):
        """Performs a Preorder Depth-First Search (DFS) to going through of binary tree

        This method uses a stack to recursive going through
        The root node is pushed in stack first -> Then, nodes are popped one by one,
        going in preorder (root -> left -> right). 
        For each "throughed" node, his right child is pushed in the stack first,
        and then left child.

        Why I am doing this - 
        because i'll be sure that the left subtree was popped before the right subtree

        Yields:
            BinaryNode: The next node in the tree, following the Preorder DFS traversal order
        """
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current: AVLNode = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            yield current

    def display(self) -> None:
        """Displays each node with indentation based on its level in the AVL tree"""
        for node in self:
            print("  " * node.level + str(node))

    def root_imbalance(self) -> str:
        """Determines the imbalance type of the tree's root node

        Makes the balance factor of the root node to determine if the tree
        is imbalanced. Based on the balance factors of the root node and his children,
        the method classifies the imbalance as one of the following types:

        - 'LL' (Left-Left): Imbalance caused by the left subtree being higher, and his left child being too high
        - 'RR' (Right-Right): Imbalance caused by the right subtree being higher, and his right child being too high
        - 'LR' (Left-Right): Imbalance caused by the left subtree being higher, and his right child being too high
        - 'RL' (Right-Left): Imbalance caused by the right subtree being higher, and his left child being too high

        If the tree is balanced, will be returned 'Balanced'

        Returns:
        str: A string describing the imbalance type ('LL', 'RR', 'LR', 'RL', or 'Balanced').
        """
        balance = self.root.balancing_factor

        if balance > 1:
            if self.root.left.balancing_factor >= 0:
                return "LL"
            else:
                return "LR"

        elif balance < -1:
            if self.root.right.balancing_factor <= 0:
                return "RR"
            else:
                return "RL"

        return "Balanced"


if __name__ == "__main__":
    from re import match

    tree = AVLTree(1)
    line_num = int(input())

    for _ in range(line_num):
        line = input()
        res = match(
            r'(?P<parent_id>\d+): (?P<left>\d+)? ?(?P<right>\d+)?\s*', line)

        if res['left']:
            tree.add_child(int(res['left']), int(res['parent_id']))
        if res['right']:
            tree.add_child(int(res['right']), int(res['parent_id']))

    print(tree.root_imbalance())
    
"""
3
0: 1 2
1: 3 4
2: 5 6
---
Balanced
"""
