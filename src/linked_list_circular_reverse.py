from httpx import head


class Node:
    def __init__(self, value):
        # value that stores the data of the node
        self.value = value
        # next that stores the reference to the next node (None by default)
        self.next = None
# example:[ apple | next → None ]

# LinkedList:
# [orange] → [apple] → [plum] → [grape] → None

# CIRCULAR LinkedList:
# [orange] → [apple] → [plum] → [grape]
#      ↑______________________________|


class CircularLinkedList:
    def __init__(self):
        # head that points to the first node in the list (None if the list is empty)
        # if the list is empty, head = None
        self.head = None

    # ====== Helper methods ======

    def _init_if_empty(self, new_node): # new_node → [orange | next = None]

        #If the list is empty, initialize it as a circular list with a single node.
        if self.head is None:
            new_node.next = new_node    # orange.next → orange → ↺ node points to itself
            self.head = new_node        # now head points to orange

            # head
            #   ↓
            # [orange]
            #   ↑
            #   └── next

            return True
        
        # If the list is not empty, do nothing and return False.
        return False

    #Find and return the last node (the one whose next points to head).
    def _get_tail(self):
        if self.head is None:
            return None

        current = self.head # current → [orange]

        # look for the node whose next points to head
        while current.next != self.head:
            current = current.next
            # step 1: current.next → [apple] != head → continue
            # step 2: current.next → [plum] != head → continue
            # step 3: current.next → [grape] != head → continue
            # step 4: current.next → [orange] == head → stop

        return current

    # ====== Main methods ======

    def insert_at_head(self, value):
        new_node = Node(value) # just create node → [value | next = None]

        # helper #1 it checks:
        # if the list is empty - initialize it as a circular list and return True
        # if the list is not empty - do nothing and return False
        if self._init_if_empty(new_node):
            return

        # helper #2
        tail = self._get_tail()

        new_node.next = self.head # new_node now points to the old head
        tail.next = new_node # the last node (tail) now points to the new node, keeping the list circular
        self.head = new_node # update head now points to the new node

    def insert_at_tail(self, value):
        new_node = Node(value) # just create node → [value | next = None]

        # helper #1
        if self._init_if_empty(new_node):
            return

        # helper #2
        tail = self._get_tail()

        tail.next = new_node # The old tail stops to be a tail, because it now points not to the head, but to the new node.
        new_node.next = self.head # New node, if you are the tail, you must look at the head

    def delete(self, value):
        # If the list is empty, there's nothing to delete
        if self.head is None:
            print("CircularLinkedList is empty — nothing to delete.")
            return False

        # indicates the current fruit from which the search begins (from the head)
        current = self.head

        # indicates the previous fruit (there is none at first -> None)
        previous = None

        # found node to delete
        while True:
            if current.value == value:

                # Case 1: only one node in the list
                if current.next == self.head and previous is None:
                    self.head = None
                    return True

                # Case 2: deleting the head
                if current == self.head:
                    # need to find the tail to update its next pointer to the new head
                    tail = self._get_tail()

                    # We move the head to the next element (fruit)
                    self.head = self.head.next

                    # now the tail should point to the new head to maintain the circular structure
                    tail.next = self.head
                    return True

                # Case 3: deleting middle or tail

                # 1. Let's say we want to delete "plum" from the middle of the list:
                # [orange] → [apple] → [plum] → [grape]
                #      ↑______________________________|
                # previous.next → [apple]   → current.next → [plum]
                # apple.next = plum.next    → apple.next = grape
                # [orange] → [apple] → [grape]
                #     ↑___________________|

                # 2. If we want to delete "grape" from the tail of the list:
                # [orange] → [apple] → [grape]
                #      ↑__________________|
                # previous.next → [apple]   → current.next → [grape]
                # apple.next = grape.next   → apple.next = orange
                # [orange] → [apple]
                #     ↑__________|

                previous.next = current.next
                return True

            # if the value is not found, we move to the next node
            # was: current=orange → becomes: previous=orange, current=apple
            # then: previous=apple, current=plum
            previous = current
            current = current.next

            # we came back to head → value not found
            if current == self.head:
                break

        print(f"Value {value} not found — nothing deleted.")
        return False

    # mothod make links reversed - that makes the list reversed
    # was:     A -> B -> C
    # become:  A <- B <- C

    # just for convinience the list displays in the reverse order
    # [orange] → [apple] → [plum] → [grape]
    #      ↑______________________________|
    
    # [grape] → [plum] → [apple] → [orange]
    #     ↑______________________________|

    def reverse(self):
        # if the list is empty or has only one element — nothing to do
        if self.head is None or self.head.next == self.head:
            return

        prev = None
        current = self.head
        start = self.head  # to know where to stop

        # because there is no None to stop, we will stop when we come back to the start
        while True:
            # remember the next node before we change the link
            next_node = current.next

            # reverse the link
            current.next = prev

            # move prev and current one step forward
            prev = current
            current = next_node

            # traversed the whole list and came back to the start → stop
            if current == start:
                break

        start.next = prev # old head (now the tail) should point to the new head (prev)
        self.head = prev  # new head after reverse

    def display(self):
        if self.head is None:
            print("CircularLinkedList: (empty)")
            return

        elements = []
        current = self.head

        while True:
            elements.append(str(current.value))
            current = current.next

            if current == self.head:
                break

        print("CircularLinkedList: " + " -> ".join(elements))


# ======== TESTS (as in the assignment) ========
if __name__ == "__main__":
    ll = CircularLinkedList()   # create an empty circular linked list

    print("\n--- TEST REVERSE ---")

    ll.insert_at_head("apple")
    ll.insert_at_head("orange")
    ll.insert_at_tail("plum")
    ll.insert_at_tail("grape")

    ll.display()

    ll.reverse()

    ll.display()

# ======== OUTPUT ========
# --- TEST REVERSE ---
# CircularLinkedList: orange -> apple -> plum -> grape
# CircularLinkedList: grape -> plum -> apple -> orange