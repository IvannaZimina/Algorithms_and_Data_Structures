"""Deque (Double-Ended Queue) implemented using an array."""

class Deque:
    def __init__(self, capacity):
        # maximum number of elements the deaue can hold
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        else:
            self.capacity = capacity

        # fixed-size array (list) -> [None, None, None] for capacity = 3
        self.deque = [None] * capacity

        self.front = 0 # Set initial front pointer first_element_index
        self.rear = 0  # Set initial rear pointer next_free_slot_after_last_element

        self.size = 0   # current amount of the elements

    # ===== Check deque status =====

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    # ===== Main methods =====

    # Add an element at the front
    def insert_front(self, value):
        # 1) check status
        if self.is_full():
            print(f"Deque is full. Can't insert {value} \n")
            return
        
        # 2) move front pointer backward (circularly)
        # (self.front - 1) - move back by one position
        # % self.capacity - recieve the correct position in a circular manner
        # (0-1) % 5 = 4, (4-1) % 5 = 3, (3-1) % 5 = 2, ...
        self.front = (self.front - 1) % self.capacity

        # 3) insert value at the new front position
        self.deque[self.front] = value

        # 4) increase size
        self.size += 1

    # Add an element at the rear
    def insert_rear(self, value):
        # 1) check status
        if self.is_full():
            print(f"Deque is full. Can't insert {value} \n")
            return

        # 2) insert value at the current rear position
        self.deque[self.rear] = value

        # 3) move rear pointer forward (circularly)
        # (self.rear + 1) - move forward by one position
        # % self.capacity - recieve the correct position in a circular manner
        # (0+1) % 5 = 1, (1+1) % 5 = 2, (2+1) % 5 = 3, ...
        self.rear = (self.rear + 1) % self.capacity

        # 4) increase size
        self.size += 1

    # Remove and return the front element
    def delete_front(self):
        # 1) check status (if empty, we cannot delete)
        if self.is_empty():
            print("Deque is empty. Nothing to delete \n")
            return

        # 2) receive value at the current front position
        value = self.deque[self.front]

        # 3) clear the value at the current front position
        self.deque[self.front] = None

        # 4) move front pointer forward (circularly)
        self.front = (self.front + 1) % self.capacity

        # 5) decrease size
        self.size -= 1
        
        print(f"Deleted from front: {value} \n")

        return value

    # Remove and return the rear element
    def delete_rear(self):
        # 1) check status (if empty, we cannot delete)
        if self.is_empty():
            print("Deque is empty. Nothing to delete \n")
            return

        # 2) move rear pointer backward (circularly)
        # rear - it is the last of the last element
        # real last element is on the position rear - 1

        # first - move rear pointer back to the real last element
        self.rear = (self.rear - 1) % self.capacity

        #second - receive value at the new rear position
        value = self.deque[self.rear]

        # 3) clear the value at the new rear position
        self.deque[self.rear] = None

        # 4) decrease size
        self.size -= 1
        print(f"Deleted from rear: {value} \n")
        return value

    # ===== View and display methods =====

    # View elements without removal
    def peek_front(self):
        # 1) check status
        if self.is_empty():
            print("Deque is empty. Nothing to peek \n")
            return
        
        # 2) return value at the current front position
        return self.deque[self.front]

    def peek_rear(self):
        # 1) check status
        if self.is_empty():
            print("Deque is empty. Nothing to peek \n")
            return

        # 2) return value at the current rear position
        return self.deque[(self.rear - 1) % self.capacity]

    # Print all elements in order
    def display(self):
        # 1) check status if empty, nothing to display)
        if self.is_empty():
            print("Deque is empty. Nothing to display \n")
            return
        
        # gather elements in order from front to rear
        elements = []

        # iterate through the deque starting from the front pointer and collect elements until the collected 'size' elements are gathered
        for i in range(self.size):
            # calculate the actual index in the circular array using modulo operation
            idx = (self.front + i) % self.capacity
            # append the element at the calculated index to the elements list
            elements.append(self.deque[idx])

        print("Deque:", elements)

    def display_internal(self):
        print("index: ", end="")
        for i in range(self.capacity):
            print(f"{i:^6}", end="")
        print()

        print("cells: ", end="")
        for cell in self.deque:
            if cell is None:
                print("[   ] ", end="")
            else:
                print(f"[{cell:^3}] ", end="")
        print()
        
        print(f"front = {self.front}, rear = {self.rear}, size = {self.size} \n")

    # ===== Example =====

    # index:  0   1   2   3   4
    # cells: [ ] [ ] [ ] [ ] [ ]
    # queue is empty, front = rear = 0
    
    # insert_rear("banana") -> value[rear] = "banana"
    # rear = (rear + 1) % capacity -> rear = (0 + 1) % 5 = 1

    # index:  0          1   2   3   4
    # cells: ["banana"] [ ] [ ] [ ] [ ]
    # front = 0, rear = 1, size = 1

# Example usage:
dq = Deque(5)
dq.display_internal()

dq.insert_front("apple")
dq.display_internal()

dq.insert_front("mango")
dq.display_internal()

dq.insert_rear("banana")
dq.display_internal()

dq.insert_rear("cherry")
dq.display_internal()

dq.insert_front("grapes")
dq.display_internal()

dq.insert_rear("peach")

dq.delete_front()
dq.display_internal()



# ===== Output =====

# index:   0     1     2     3     4   
# cells: [   ] [   ] [   ] [   ] [   ] 
# front = 0, rear = 0, size = 0 

# index:   0     1     2     3     4   
# cells: [   ] [   ] [   ] [   ] [apple] 
# front = 4, rear = 0, size = 1 

# index:   0     1     2     3     4   
# cells: [   ] [   ] [   ] [mango] [apple] 
# front = 3, rear = 0, size = 2 

# index:   0         1     2     3     4   
# cells: [banana] [   ] [   ] [mango] [apple] 
# front = 3, rear = 1, size = 3 

# index:   0         1     2     3     4   
# cells: [banana] [cherry] [   ] [mango] [apple] 
# front = 3, rear = 2, size = 4 

# index:   0         1         2        3     4   
# cells: [banana] [cherry] [grapes] [mango] [apple] 
# front = 2, rear = 2, size = 5 

# Deque is full. Can't insert peach 

# Deleted from front: grapes 

# index:   0        1        2       3     4   
# cells: [banana] [cherry] [   ] [mango] [apple] 
# front = 3, rear = 2, size = 4 
