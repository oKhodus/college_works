class CircularQueue:
    def __init__(self, capacity):
        """
        _summary_

        Args:
            capacity (int): _description_
        """
        self.capacity = capacity  # TODO: Initialize the queue
        self.queue = [None] * capacity  # TODO: Create a fixed-size list
        self.front = -1  # TODO: Set initial front pointer
        self.rear = -1  # TODO: Set initial rear pointer

    def is_empty(self):
        """_summary_"""
        # TODO: Check if the queue is empty
        return self.front == -1
        # return self.front == -1 and self.rear == -1

    def is_full(self):
        """_summary_"""
        # TODO: Check if the queue is full
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, value):
        """_summary_"""
        # TODO: Implement enqueue operation
        if self.is_full():
            raise IndexError("Oioioi, Queue is full")

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = value

    def dequeue(self):
        """_summary_"""
        # TODO: Implement dequeue operation
        if self.is_empty():
            raise IndexError
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear - 1
        else:
            self.front = (self.front + 1) % self.capacity
        return value
    
    def peek(self):
        """_summary_"""
        # TODO: Return the front element without removing it
        return self.queue[self.front]

    def display(self):
        """_summary_"""
        # TODO: Display all elements in the queue
        if self.is_empty():
            return
        all = []
        index = self.front
        while True:
            all.append(self.queue[index])
            if index == self.rear:
                break
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


cq.dequeue()
cq.display()

cq.enqueue(6)
cq.display()
