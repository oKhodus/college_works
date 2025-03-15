class Deque:
    def __init__(self, capacity):
        """
        Initialize the deque with a fixed capacity

        Args:
            capacity (int): The maximum size of the deque
        """
        # Set the maximum capacity of the q
        self.capacity = capacity  # TODO: Initialize the queue
        # Create a ls with NONE to hold the elements of the q
        self.deque = [None] * capacity  # TODO: Create a fixed-size list
        # front pointer starts at -1 - shows that the q is empty
        self.front = -1  # TODO: Set initial front pointer
        # rear pointer starts at -1 - shows that the q is empty
        self.rear = -1  # TODO: Set initial rear pointer

    def is_empty(self):
        """Check if the queue is empty"""
        # TODO: Check if the queue is empty
        # The q is empty if front is -1
        return self.front == -1

    def is_full(self):
        """Check if the queue is full"""
        # TODO: Check if the queue is full
        # The q is full when the next position after the rear == front position
        return (self.rear + 1) % self.capacity == self.front

    def insert_front(self, value):
        """Insert an element at the front of the deque"""
        if self.is_full():
            raise IndexError("Oioioi, Queue is full")

        if self.is_empty():
            # if the dq is empty, both front and rear are set to 0 (1st element)
            self.front = self.rear = 0
        else:
            # move front pointer to the prev position
            self.front = (self.front - 1) % self.capacity
        # insert value at the front of the dq
        self.deque[self.front] = value

    def insert_rear(self, value):
        """Insert an element at the rear of the deque"""
        if self.is_full():
            raise IndexError("Oioioi, Queue is full")

        if self.is_empty():
            # if the dq is empty - both front and rear are set to 0 (1st element)
            self.front = self.rear = 0
        else:
            # move front pointer to the next position
            self.rear = (self.rear + 1) % self.capacity
        # insert value at the rear of the dq
        self.deque[self.rear] = value

    def delete_front(self):
        """Remove and return the front element"""
        if self.is_empty():
            raise IndexError("Deque is empty, cannot delete from front")
        # Get value at the front of the dq
        value = self.deque[self.front]

        if self.front == self.rear:
            # if only 1 elem - reset both front and rear to -1 (empty dq)
            self.front = self.rear = -1
        else:
            # move front pointer to the next pos
            self.front = (self.front + 1) % self.capacity

        return value

    def delete_rear(self):
        """Remove and return the rear element"""
        if self.is_empty():
            raise IndexError("Deque is empty, cannot delete from rear")
        # Get value at the rear of the dq
        value = self.deque[self.rear]

        if self.front == self.rear:
            # if only 1 elem  - reset both front and rear to -1 (empty dq)
            self.front = self.rear = -1
        else:
            # move the rear pointer to the prev pos
            self.rear = (self.rear - 1) % self.capacity

        return value

    def peek_front(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty, cannot peek from front")
        # raeturn elem at the front without removing it
        return self.deque[self.front]

    def peek_rear(self):
        """Return the rear element without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty, cannot peek from rear")
        # return elem at the rear without removing it
        return self.deque[self.rear]

    def display(self):
        """Display all elements in the deque."""
        if self.is_empty():
            return

        all = []
        index = self.front
        while True:
            all.append(self.deque[index])
            if index == self.rear:
                break
            index = (index + 1) % self.capacity  # move to the next elem
        print(f"DQ: {all}")


# Example usage:
dq = Deque(5)
dq.insert_rear(1)
dq.insert_rear(2)
dq.insert_front(0)
dq.display()

"""Display the deque: [0, 1, 2]"""

dq.delete_front()
dq.display()
"""Display the deque: [1, 2]"""
dq.insert_front(-1)
dq.insert_rear(3)
dq.display()
"""Display the deque: [-1, 1, 2, 3]"""
