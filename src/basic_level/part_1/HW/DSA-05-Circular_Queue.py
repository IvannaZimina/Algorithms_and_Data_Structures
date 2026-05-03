class CircularQueue:
    # 1. Initialize the queue with a fixed capacity.
    def __init__(self, capacity):
        self.capacity = capacity  # stores the maximum queue size.

        # additional: creates a fixed-length list (array) that does not change in size.
        self.queue = [None] * capacity
        # front points to the first element, rear points to the next insertion position
        self.front = 0
        self.rear = 0

    # ========== 2.4. Check queue status ==========

    def is_empty(self):
        # Returns True if the queue is empty, False otherwise.
        return self.front == self.rear

    def is_full(self):
        # Calculates the index where the next element will be placed.
        # If this index matches self.front, then there is no free space—the queue is full.
        return (self.rear + 1) % self.capacity == self.front

    # ========== Main operations ==========

    # 2.1. Add an element if space is available.
    def enqueue(self, value):
        # Check if the queue is full before adding a new element.
        # If it is full, print a message and return without adding the element.
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        
        # Insert a new element at position rear.
        self.queue[self.rear] = value

        # Move rear forward in a circle (wrap-around).
        self.rear = (self.rear + 1) % self.capacity

    # 2.2. Remove and return the front element.
    def dequeue(self):
        # check if the queue is empty before trying to remove an element.
        # If it is empty, print a message and return None.
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        
        # Stores the value of the first element of the queue -
        # the one that will be removed
        value = self.queue[self.front]

        # Move front forward in a circle (wrap-around).
        self.front = (self.front + 1) % self.capacity

        # Return the removed element.
        return value

    # 2.3. Return the front element without removing it.
    def peek(self):
        # Check whether the queue is empty.
        # If so, print a message and return None - nothing to peek.
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        
        # If the queue is not empty, return the value of the first element without removing it from the queue.
        return self.queue[self.front]

    # ======== Display method for testing purposes ========

    # 2.5. Print all queue elements in order.
    def display(self):
        # Check whether the queue is empty.
        # If so, print a message and terminate the method.
        if self.is_empty():
            print("Queue is empty.")
            return
        
        # Set index i to the front of the queue.
        i = self.front

        # Create an empty list to store the queue elements.
        elements = []

        # Traverse the queue from front to rear (wrap-around).
        while i != self.rear:
            # Append the current queue element (at index i) to the elements list.
            elements.append(self.queue[i])

            # Shift index i forward in a wrap-around fashion to correctly traverse the circular queue.
            i = (i + 1) % self.capacity
        print("Queue:", elements)


# Example usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
# This enqueue will not add the element, as the queue is full (max 4 elements for capacity=5)
cq.enqueue(5)
cq.display()  # Queue: [1, 2, 3, 4]
cq.dequeue()
cq.display()  # Queue: [2, 3, 4]
cq.enqueue(6)
cq.display()  # Queue: [2, 3, 4, 6]
