class Deque:
    def __init__(self, capacity):
        """Initialize the deque with a fixed capacity"""
        # fixed size of elements, meaning that deque cannot grow beyond this capacity.
        self.capacity = capacity

        # additional: python list can be used instead of DoublyLinkedList for simplicity
        self.deque = [None] * capacity

        self.front = -1  # Set initial front pointer
        self.rear = -1  # Set initial rear pointer

    # ====== 2.6. Check deque status ======

    def is_empty(self):
        """ Check if the deque is empty"""

        # True if front is -1 (no elements are present in the deque), False otherwise.
        return self.front == -1

    def is_full(self):
        """ Check if the deque is full """
        # (self.rear + 1) -> calculates the next index where a new element would be added
        # % self.capacity -> makes the index wrap around to the beginning if needed
        # If this next position is equal to front, it means there is no free space left
        # In this case, the deque is full
        return (self.rear + 1) % self.capacity == self.front

    # ========== Helper method ==========

    def _prepare_insert(self):
        """Check capacity and initialize pointers for first insert"""
        # check if the deque is full before trying to insert an element.
        if self.is_full():
            raise OverflowError("Deque is full")

        # check if the deque is empty before trying to insert an element.
        if self.is_empty():
            # the beginning and end of the deque point to the same index - 0
            self.front = self.rear = 0
            return True

        return False
    
    def _prepare_delete(self):
        """Check if deque is empty before deletion"""
        if self.is_empty():
            raise IndexError("Deque is empty")

    def _clear_if_last(self):
        """Reset pointers when only one element remains"""
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        return False

    # ====== Main operations ======

    # 2.1 Add an element at the front.
    def insert_front(self, value):
        if not self._prepare_insert():
            # self.front - 1: Shifts front back one position
            # % self.capacity: If front was at 0, it will jump to the end of the array
            # front points to the new insertion location.
            self.front = (self.front - 1) % self.capacity

        self.deque[self.front] = value

    # 2.2. Add an element at the rear.
    def insert_rear(self, value):
        if not self._prepare_insert():
            # self.rear + 1: Moves rear one position forward
            # % self.capacity: If rear was at the end of the array, it will jump to the beginning
            # rear points to the next insertion location
            self.rear = (self.rear + 1) % self.capacity

        self.deque[self.rear] = value

    # 2.3. Remove and return the front element.
    def delete_front(self):
        # check if the deque is empty before trying to remove an element.
        self._prepare_delete()

        # store an element from the deque array at the front index
        value = self.deque[self.front]

        if not self._clear_if_last():
            # If there is more than one element, remove the first one.
            # front + 1: shift the pointer to the next element.
            # % self.capacity: if this was the end of the array, move to the beginning (wrap-around).
            self.front = (self.front + 1) % self.capacity
        return value

    # 2.4. Remove and return the rear element.
    def delete_rear(self):
        # check if the deque is empty before trying to remove an element.
        self._prepare_delete()

        # store an element from the deque array at the rear index
        value = self.deque[self.rear]

        if not self._clear_if_last():
            # If there is more than one element, remove the last one.
            # rear - 1: move backward through the array.
            # % self.capacity: if rear was 0, it will jump to the end of the array.
            self.rear = (self.rear - 1) % self.capacity
        return value

    # ========= 2.5. View elements without removal ======

    def peek_front(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[self.front]

    def peek_rear(self):
        """Return the rear element without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[self.rear]

    # ====== 2.6. Print all elements in order. ======

    def display(self):
        """Display all elements in the deque"""
        if self.is_empty():
            print("Deque is empty")
        elif self.rear >= self.front:
            print("Deque elements:", self.deque[self.front:self.rear + 1])
        else:
            print("Deque elements:", self.deque[self.front:] + self.deque[:self.rear + 1])


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

# ===== Expected Output =====
# Deque elements: [0, 1, 2]
# Deque elements: [1, 2]
# Deque elements: [-1, 1, 2, 3]