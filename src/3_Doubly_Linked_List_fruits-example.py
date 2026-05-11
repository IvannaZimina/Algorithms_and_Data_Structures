class Node:
    def __init__(self, value):
        # prev <- [ banana ] -> next
        self.value = value   # attribute to store data (example "banana")
        self.next = None     # pointer linking to the next node.
        self.prev = None     # pointer linking to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # pointer to the first node in the list
        self.tail = None  # pointer to the last node in the list

    # ==== HELPER ====
    def _insert_into_empty_list(self, new_node):
        # if the list is empty: head = None, tail = None.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return True
        return False


    def insert_at_head(self, value):
        new_node = Node(value) # new_node → [kiwi | next = None, prev = None]

        # 1) if the list is empty - the new node becomes both head and tail
        if self._insert_into_empty_list(new_node):
            return

        # 2) if the list is not empty
        new_node.next = self.head      # old head becomes the next node for the new node: new -> old head
        self.head.prev = new_node      # new node becomes the previous node for the old head: new <- old head
        self.head = new_node           # head now points to the new node

    def insert_at_tail(self, value):
        new_node = Node(value) # new_node → [grape | next = None, prev = None]

        # 1) if the list is empty - the new node becomes both head and tail
        if self._insert_into_empty_list(new_node):
            return

        # 2) if the list is not empty
        self.tail.next = new_node      # old tail -> new
        new_node.prev = self.tail      # new <- old tail
        self.tail = new_node           # tail now points to the new node

    def delete(self, value):
        # If the list is empty, there's nothing to delete
        if self.head is None:
            return False

        # element which we want to delete, but first to find it
        current = self.head

        # Look for the node to delete
        while current is not None and current.value != value:
            current = current.next

        # If not found
        if current is None:
            return False

        # Case 1: delete head
        if current == self.head:
            self.head = current.next  # shift head to the right, now next node is the head

            # And there are two variants for the new head:
            if self.head is not None: # if the element is not the only one in the list
                self.head.prev = None # than the next node is None (only one element on the list)
            else:
                # if head became None, it means the list is now empty
                self.tail = None
            return True

        # Case 2: delete tail
        if current == self.tail:
            self.tail = current.prev    # shift tail to the left, now the previous node is the tail
            self.tail.next = None       # the next element after shifting becomes None
            return True

        # Case 3: delete node in the middle

        # head       node to remove    tail
        #  ↓            ↓               ↓
        # [apple] <-> [banana] <-> [cherry] <-> [date]

        # current → [banana] - we want to remove
        # prev_node → [apple]
        # next_node → [cherry]

        prev_node = current.prev # just remeber the reference to the previous node (apple)
        next_node = current.next # just remeber the reference to the next node (cherry)

        # through changing the references - we delete the element from the list, because no one points to it anymore
        prev_node.next = next_node    # left -> right   [apple].next -> [cherry]
        next_node.prev = prev_node    # right <- left   [cherry].prev -> [apple]

        return True

    # Print the list from head to tail (using next pointers)
    def display_forward(self):
        """
        Shows how the list looks when traversing
        from head to tail using `next` references.
        """
        current = self.head
        values = []

        while current is not None:
            values.append(current.value)
            current = current.next

        print("FORWARD (head -> tail):",
            " -> ".join(values) if values else "(empty)")


    # Print the list from tail to head (using prev pointers)
    def display_backward(self):
        """
        Shows how the list looks when traversing
        from tail to head using `prev` references.
        """
        current = self.tail
        values = []

        while current is not None:
            values.append(current.value)
            current = current.prev

        print("BACKWARD (tail -> head):",
            " <- ".join(values) if values else "(empty)")


# ====== TESTS WITH CLEAR MEANING ======

print("===== CREATE LIST AND INSERT ELEMENTS AT TAIL =====")

fruits = ["apple", "banana", "cherry", "date"]
dll = DoublyLinkedList()

print("Insert fruits at tail one by one:")
for fruit in fruits:
    print(f"  inserting '{fruit}' at tail")
    dll.insert_at_tail(fruit) # [apple] -> [banana] -> [cherry] -> [date]

print("\nCurrent list (should show all fruits):")
dll.display_forward()     # from apple to date [apple -> banana -> cherry -> date]
dll.display_backward()    # from date to apple [date <- cherry <- banana <- apple]


print("\n===== DELETE A MIDDLE ELEMENT =====")
print("Delete 'banana' (middle element):")

dll.delete("banana")

print("\nList after deleting 'banana':")
dll.display_forward()     # apple -> cherry -> date
dll.display_backward()    # date <- cherry <- apple


print("\n===== INSERT ELEMENT AT HEAD =====")
print("Insert 'kiwi' at head:")

dll.insert_at_head("kiwi")

print("\nList after inserting 'kiwi' at head:")
dll.display_forward()     # kiwi -> apple -> cherry -> date
dll.display_backward()    # date <- cherry <- apple <- kiwi


print("\n===== EDGE CASE: DELETE ONLY NODE =====")
single = DoublyLinkedList()

print("Insert a single element 'mango':")
single.insert_at_head("mango")

single.display_forward()  # mango
single.display_backward() # mango

print("\nDelete the only element 'mango':")
single.delete("mango")

print("\nList after deleting the only element:")
single.display_forward()   # (empty)
single.display_backward()  # (empty)