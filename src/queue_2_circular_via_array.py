class CircularQueue:
    def __init__(self, capacity):
        # fixed-size array (list)
        self.queue = [None] * capacity  # [None, None, None] for capacity = 3
        self.capacity = capacity        # maximum number of elements the queue can hold

        self.front = 0   # index of the front element
        self.rear = -1   # points to the last element (initially -1 since the queue is empty)
        self.size = 0    # current number of elements

    # Check if queue is empty
    def is_empty(self):
        return self.size == 0

    # Check if queue is full
    def is_full(self):
        return self.size == self.capacity

    # Add element to the queue
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full — cannot enqueue")
            return False

        # move rear in circular way
        self.rear = (self.rear + 1) % self.capacity
        # (-1+1) % 5 = 0
        # (0+1) % 5 = 1
        # (1+1) % 5 = 2 etc.

        # only if self.size < self.capacity
        # insert value by rear "index": self.queue[0] = 1
        self.queue[self.rear] = value
        self.size += 1

        print(f"Enqueued: {value}")
        return True

    # Remove element from the head of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty — cannot dequeue")
            return None

        value = self.queue[self.front]  # get the front element to return it later
        self.queue[self.front] = None   # clear the slot explicitly

        # move front in circular way
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued: {value}")
        return value

    # Return front element without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty — no front element")
            return None
        return self.queue[self.front]

    # Display queue elements in correct order
    def display(self):
        if self.is_empty():
            print("Queue: (empty)")
            return

        index = self.front

        for _ in range(self.size):
            index = (index + 1) % self.capacity

        print(f"Queue: {self.queue}")

if __name__ == "__main__":
    cq = CircularQueue(5)

cq.enqueue("apple")
cq.display()
cq.enqueue("banana")
cq.display()
cq.enqueue("cherry")
cq.display()

cq.dequeue()
cq.display()
cq.dequeue()
cq.display()
cq.dequeue()
cq.display()
cq.display()

cq.enqueue("date")
cq.display()
cq.enqueue("grape")
cq.display()
cq.enqueue("kiwi")
cq.display()
cq.enqueue("mango")
cq.display()

# ==== Output ====
# Enqueued: apple
# Queue: ['apple', None, None, None, None]
# Enqueued: banana
# Queue: ['apple', 'banana', None, None, None]
# Enqueued: cherry
# Queue: ['apple', 'banana', 'cherry', None, None]
# Dequeued: apple
# Queue: [None, 'banana', 'cherry', None, None]
# Dequeued: banana
# Queue: [None, None, 'cherry', None, None]
# Dequeued: cherry
# Queue: (empty)
# Queue: (empty)
# Enqueued: date
# Queue: [None, None, None, 'date', None]
# Enqueued: grape
# Queue: [None, None, None, 'date', 'grape']
# Enqueued: kiwi
# Queue: ['kiwi', None, None, 'date', 'grape']
# Enqueued: mango
# Queue: ['kiwi', 'mango', None, 'date', 'grape']