from typing import Any, Type


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
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
    def __init__(self, node_id: int, data: Any, parent: Type['Node'] = None) -> None:
        self.id = node_id
        self.data = data
        self.parent = parent
        self.child = []

    def __repr__(self) -> str:
        return f"N{self.id}({self.data})"


class Tree:
    def __init__(self, root_data: Any) -> None:
        self.root = Node(0, root_data)
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node_id: int = 0) -> Node:
        parent = self.map[to_node_id]
        last_id = len(self.map)
        new_node = Node(last_id, child_data, parent)
        parent.child.append(new_node)
        self.map[last_id] = new_node
        return new_node

    def __iter__(self):
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current: Node = stack.pop()
            for child in current.child:
                stack.push(child)
            yield current

    def height(self, node_id: int) -> int:
        """Returns height of tree starting from the given node"""
        # get node from map using node_id
        node = self.map[node_id]

        # if node doesn't have children - it's a leaf and will return height 0
        if not node.child:
            return 0

        # Recursively calculate height of each child
        child_heights = [self.height(child.id) for child in node.child]

        # height of node is 1 + max height of his children
        return 1 + max(child_heights)


if __name__ == "__main__":
    tree = Tree('A')
    B = tree.add_child('B')  
    C = tree.add_child('C')
    tree.add_child('D', B.id)
    tree.add_child('E', B.id)
    F = tree.add_child('F', C.id)
    G = tree.add_child('G', F.id)

     # input node id whose height i want
    node_id = int(input())
    print(tree.height(node_id))

"""
examples:

if enter 2 -> out = 2
because B has 2 children (d, e) both are leaf nodes so their height is 0

if enter 4 it is D - it will return 0 - because it is a leaf node
"""