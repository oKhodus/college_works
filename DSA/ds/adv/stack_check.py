from typing import Any

class Stack:
    """Implements stack with bracket balancing functionality"""
    def __init__(self):
        """Initializes an empty stack and defines dictionary of matching bracket pairs"""
        self.stack = []
        self.bracket_pairs = {")": "(", "]": "[", "}": "{"}
    
    def push(self, item):
        """Pushes an item in stack

        Args:
            item (Any): element which will be added
        """
        self.stack.append(item)

    def pop(self):
        """Removes and returns the top element of the stack

        Returns:
            The last pushed element or None if stack is empty
        """
        if self.stack is None:
            return None
        return self.stack.pop()

    def peek(self):
        """
        Returns top element of stack without removing it

        Returns: 
            The top element of stack or None if stack is empty
        """
        if self.is_empty():
            return None
        # get the last elem without rm it
        return self.stack[-1]

    def is_empty(self):
        """Check if stack is empty

        Returns:
            bool: True if stack is empty else False
        """
        return len(self.stack) == 0
    
    def is_brackets_balanced(self, expr: str) -> bool:
        """Checks if brackets in given expression are balanced

        Args:
            expr (str): String containing brackets and other chars' 

        Returns:
            bool: True if brackets is balanced else False
        Logic:
        - Open brackets ('(', '[', '{') are pushed in stack
        - Closing brackets (')', ']', '}') check if top of stack has matching opening bracket
        - If a mismatch was found or stack is empty when expecting an opening bracket will return False
        """
        for bracket in expr:
            # if it's an opening bracket
            if bracket in self.bracket_pairs.values():
                self.push(bracket)
            # if it's a closing bracket
            elif bracket in self.bracket_pairs:
                # check for a match
                if self.is_empty() or self.pop() != self.bracket_pairs[bracket]:
                    return False
        # if stack empty -brackets balanced
        return self.is_empty()
        
stack = Stack()
print(stack.is_brackets_balanced("[(abc)]{a}{[(b)(42)]*(56)}"))
"""True"""
print(stack.is_brackets_balanced("[(abc])"))
"""False"""
print(stack.is_brackets_balanced("[](){}{}{}{}{}{}"))
"""True"""