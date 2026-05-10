class Node:
    def __init__(self, value):
        # value that stores the data of the node
        self.value = value
        # next that stores the reference to the next node (None by default)
        self.next = None
# example:[ apple | next → None ]

class LinkedList:
    def __init__(self):
        # head that points to the first node in the list (None if the list is empty)
        # if the list is empty, head = None
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value) # just create node → [orange | next = None]

        # current head becomes the second node in the list
        new_node.next = self.head # remember old head [orange | next → apple]

        # Now the new node becomes the head: head → orange
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value) # just create node → [grape | next = None]

        # self.head → [orange] → [apple] → [plum] → None
        # new_node  → [grape | None]

        # If the list is empty — the new node becomes both the head and the tail
        if self.head is None:
            self.head = new_node
            return

        current = self.head # current head → [orange]

        # goes from the head to the last node (the one whose next is None)
        while current.next is not None:
            current = current.next
            # [orange] → [apple] → [plum] → [grape] → None
            # when None is reached, condition is not satisfied and the loop stops

        # now current — the last node, so it connects to the new node
        current.next = new_node # [orange] → [apple] → [plum] → [grape] → None

    def delete(self, value):
        # If the list is empty, there's nothing to delete
        if self.head is None:
            print("LinkedList is empty — nothing to delete.")
            return False

        # 1) Common case: deleting the head
        # If the value in the head matches — just assign the head to the next node
        if self.head.value == value: # was: [orange] → [apple] → [plum] → [grape] → None
            self.head = self.head.next # now head → [apple] → [plum] → [grape] → None
            return True

        # 2) Deleting a node that is not the head

        previous = self.head        # head is the [orange]
        current = self.head.next    # [apple] is the next node after head [orange]

        # previous (self.head) → [orange] → [apple] → [plum] → [grape] → None
        #                                       ↑
        #                                    current (self.head.next)

        # We traverse the list until we find the node to delete (in the tail or in the middle)
        while current is not None:
            # if the element is found from the first step - just remove it by connecting the previous node to the next node
            # if the element is not found from the first step - skip this condition
            if current.value == value:          # [plum] == [plum]
                previous.next = current.next    # after [apple] becomes → [grape]
                # we assigned new arrangement in the list, so the plum is no more existing in the list, and the previous node [apple] is now connected to the next node [grape]
                return True

            previous = current      # [orange] becomes → [apple]
            current = current.next  # [apple] becomes → [plum]

            # and after this the condition if current.value == value: → [plum] == [plum] is True

            # head → [orange] → [apple] → [plum] → [grape] → None
            #                       ↑        ↑
            #                    previous   current

        # If we reached here — the value was not found
        print(f"Value {value} not found — nothing deleted.")
        return False

    def display(self):
        if self.head is None:
            print("LinkedList: (empty)")
            return

        # Collect values in a list to display them nicely
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.value))
            current = current.next

        print("LinkedList: " + " -> ".join(elements))


# ======== TESTS (as in the assignment) ========
if __name__ == "__main__":
    ll = LinkedList()   # create an empty linked list
    ll.display()        # should show that the list is empty

    # Checking deletion from an empty list
    ll.delete("apple")       # should print a message that the list is empty and nothing is deleted
    ll.display()        # should still show that the list is empty

    # Insertions
    ll.insert_at_head("apple")      # list: apple
    ll.insert_at_head("orange")     # list: orange -> apple
    ll.insert_at_tail("plum")       # list: orange -> apple -> plum
    ll.insert_at_tail("grape")      # list: orange -> apple -> plum -> grape
    ll.display()

    # Deletion from the middle
    ll.delete("plum")               # list: orange -> apple -> grape
    ll.display()

    # Deletion of the head
    ll.delete("orange")             # list: apple -> grape
    ll.display()

    # Deletion of the tail
    ll.delete("grape")              # list: apple
    ll.display()

    # Deletion of the only node
    ll.delete("apple")              # list: (empty)
    ll.display()

    # Deletion of a non-existent value
    ll.delete("grape")
