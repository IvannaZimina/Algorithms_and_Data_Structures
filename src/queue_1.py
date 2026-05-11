class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# FIFO - First In First Out
class Queue:
    def __init__(self):
        self.front = None   # the first node in the queue (head)
        self.rear = None    # the last node in the queue (tail)
        self.size = 0       # the number of elements in the queue

    # O(1)
    def __len__(self):
        return self.size
    
    # O(n)
    def __repr__(self): # represantation
        items = []
        current_item = self.front

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return f"Queue({' → '.join(items)})"

    # O(1)
    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None: # if the queue is empty
            self.front = self.rear = new_node # the node becomes both the front and rear of the queue
        else:
            self.rear.next = new_node   # old tail now points to the new node
            self.rear = new_node        # new node becomes the new tail of the queue
        
        self.size += 1

    # O(1)
    def dequeue(self):
        if self.front is None: # if the queue is empty
            raise IndexError("Queue is empty")

        dequeue_value = self.front.value # store the value to return later
        self.front = self.front.next     # move the front pointer to the next node

        if self.front is None:  # if the queue is now empty after dequeue
            self.rear = None    # set rear (tail) to None as well

        self.size -= 1
        return dequeue_value 

    # O(1)
    # return the value without removing it from the queue
    def peek(self):
        if self.front is None: # if the queue is empty
            raise IndexError("Queue is empty")
        return self.front.value

    # O(1)
    def is_empty(self):
        return self.front is None

if __name__ == "__main__":
    queue = Queue()
    print(queue)  # Queue()

    queue.enqueue(10)
    print(queue)  # Queue(10)

    queue.enqueue(20)
    print(queue)  # Queue(10 → 20)

    queue.enqueue(30)
    print(queue)  # Queue(10 → 20 → 30)
    print(len(queue)) # 3

    print(queue.dequeue())  # 10
    print(queue)            # Queue(20 → 30)

    print(queue.peek())     # 20
    print(queue.is_empty()) # False

    print(queue.dequeue())  # 20
    print(queue.dequeue())  # 30
    print(queue.is_empty()) # True

    try:
        queue.dequeue()     # should raise an error
    except IndexError as e:
        print(e)           # Queue is empty