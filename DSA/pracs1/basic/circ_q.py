class CircularQueue:
    def __init__(self, capacity):
        """
        Initialize the circular queue with a given capacity

        Args:
            capacity (int): maximum size of the queue
        """
        # Set the maximum capacity of the q
        self.capacity = capacity  # TODO: Initialize the queue
        # Create a ls with NONE to hold the elements of the q
        self.queue = [None] * capacity  # TODO: Create a fixed-size list
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

    def enqueue(self, value):
        """Insert an element into the queue"""
        # TODO: Implement enqueue operation
        if self.is_full():
            raise IndexError("Oioioi, Queue is full")

        if self.is_empty():
            # if the q is empty - set both front and rear to 0 (1st element)
            self.front = self.rear = 0
        else:
            # refresh rear pointer by module
            self.rear = (self.rear + 1) % self.capacity

        # place new elem at the rear pos
        self.queue[self.rear] = value

    def dequeue(self):
        """Remove an element from the front of the queue"""
        # TODO: Implement dequeue operation
        if self.is_empty():
            raise IndexError("Queue is empty - cannot dequeue")
        # Get the value from the front of the queue
        value = self.queue[self.front]
        if self.front == self.rear:
            # if the q has only 1 elem -refresh both to -1
            self.front = self.rear - 1
        else:
            # of not - move the front pointer
            self.front = (self.front + 1) % self.capacity
        return value

    def peek(self):
        """Return the front element without removing it"""
        # TODO: Return the front element without removing it
        return self.queue[self.front]

    def display(self):
        """Display all elements in the queue"""
        # TODO: Display all elements in the queue
        if self.is_empty():
            return
        all = []
        index = self.front
        while True:
            all.append(self.queue[index])
            if index == self.rear:
                break
            # Move to the next element by module
            index = (index + 1) % self.capacity
        print(f"Q: {all}")


# Example usage:
cq = CircularQueue(5)
# cq.enqueue(1)
# cq.enqueue(2)
# cq.enqueue(3)
# cq.enqueue(4)
# cq.enqueue(5)
for elem in range(1, 6):
    cq.enqueue(elem)
cq.display()
"""Display the queue: [1, 2, 3, 4, 5]"""


cq.dequeue()
cq.display()
"""Display the queue: [2, 3, 4, 5]"""

cq.enqueue(6)
cq.display()
"""Display the queue: [2, 3, 4, 5, 6]"""
