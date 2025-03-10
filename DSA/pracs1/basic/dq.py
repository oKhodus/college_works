class Deque:
    def __init__(self, capacity):
        """
        _summary_

        Args:
            capacity (int): _summary_
        """
        self.capacity = capacity  # TODO: Initialize the deque with a fixed capacity
        self.deque = [None] * capacity  # TODO: Create a fixed-size list
        self.front = -1  # TODO: Set initial front pointer
        self.rear = -1  # TODO: Set initial rear pointer

    def is_empty(self):
        """_summary_"""
        # TODO: Check if the deque is empty
        return self.front == -1

    def is_full(self):
        """_summary_"""
        # TODO: Check if the deque is full
        return (self.rear + 1) % self.capacity == self.front

    def insert_front(self, value):
        """_summary_"""
        # TODO: Insert an element at the front of the deque
        if self.is_full():
            raise IndexError

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity

        self.deque[self.front] = value
         

    def insert_rear(self, value):
        """_summary_"""
        # TODO: Insert an element at the rear of the deque
        if self.is_full():
            raise IndexError

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.deque[self.rear] = value

    def delete_front(self):
        """_summary_"""
        # TODO: Remove and return the front element
        if self.is_empty():
            raise IndexError
        
        value = self.deque[self.front]

        if self.front == self.rear:
            self.front = self.rear - 1
        else:
            self.front = (self.front + 1) % self.capacity

        return value

    def delete_rear(self):
        """_summary_"""
        # TODO: Remove and return the rear element
        if self.is_empty():
            raise IndexError
        
        value = self.deque[self.rear]

        if self.front == self.rear:
            self.front = self.rear - 1
        else:
            self.rear = (self.rear + 1) % self.capacity

        return value

    def peek_front(self):
        """_summary_"""
        # TODO: Return the front element without removing it
        if self.is_empty():
            raise IndexError
        
        return self.deque[self.front]
    
    def peek_rear(self):
        """_summary_"""
        # TODO: Return the rear element without removing it
        if self.is_empty():
            raise IndexError
        
        return self.deque[self.rear]

    def display(self):
        """_summary_"""
        # TODO: Display all elements in the deque
        if self.is_empty():
            return

        all = []
        index = self.front
        while True:
            all.append(self.deque[index])
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print(f"DQ: {all}")


# Example usage:
dq = Deque(5)
dq.insert_rear(1)
dq.insert_rear(2)
dq.insert_front(0)
dq.display()

dq.delete_front()
dq.display()

dq.insert_front(-1)
dq.insert_rear(3)
dq.display()
