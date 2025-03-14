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
            
    def degree(self, node_id: int) -> int:
        node = self.map[node_id]
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

