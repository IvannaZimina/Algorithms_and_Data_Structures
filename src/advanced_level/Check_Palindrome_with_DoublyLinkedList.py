# Replace # TODO: with your code

class Node:
    def __init__(self, value):
        """
        Simple node for doubly linked list.
        Attributes:
            value: value stored in node
            next: pointer to next node
            prev: pointer to previous node
        """
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    # Initialize empty list with head and tail.
    def __init__(self):
        self.head = None
        self.tail = None

    # ================== Helpers ==================

    # helper: initialize the list with one node (head and tail are the same)
    # use in insert_at_head and insert_at_tail when list is empty
    def _set_single_node(self, node: Node):
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        return True

    # ================== Main Methods ==================

    # 2.1. insert new node at the beginning (head)
    def insert_at_head(self, value):
        # make new node
        new_node = Node(value)

        # if the list is empty, make this node the only element
        if not self.head:
            return self._set_single_node(new_node)
        
        # the new node points to the current head
        new_node.next = self.head

        # the old head now points back to the new node.
        self.head.prev = new_node

        # update head to new node
        self.head = new_node

        return True

    # 2.2. insert new node at the end (tail)
    def insert_at_tail(self, value):
        # make new node
        new_node = Node(value)

        # if the list is empty, make this node the only element
        if not self.tail:
            return self._set_single_node(new_node)

        # the current tail points to the new node
        self.tail.next = new_node

        # the new node points back to the current tail
        new_node.prev = self.tail

        # update tail to new node
        self.tail = new_node

        return True

    # 2.3. Remove a node with the given value.
    def delete(self, value):
        # 3.3. check for empty list
        if not self.head:
            return False

        # store the head node for traversal
        node = self.head

        # move forward until the value is found or reach the end
        while node and node.value != value:
            node = node.next

        # check if node with value was found
        if not node:
            return False

        # === To correctly remove a node and preserve the list links in all cases, checks are needed: ===

        # if this is not the head, skip it by linking prev -> next
        if node.prev:
            node.prev.next = node.next
        else:
            # if this is the head, move head to the next node
            self.head = node.next

        # if this is not the tail, skip it by linking next -> prev
        if node.next:
            node.next.prev = node.prev
        else:
            # if this is the tail, move tail to the previous node
            self.tail = node.prev

        # clear node's next and prev to fully remove it from the list
        node.prev = None
        node.next = None

        return True

    # This method checks whether a list is a palindrome
    # (with the same elements at the beginning and end).
    def is_palindrome(self) -> bool:
        left = self.head    # the left pointer is set to the head of the list
        right = self.tail   # the right pointer is set to the tail of the list

        # the loop continues as long as left and right are not None,
        # and they have not met or crossed each other
        while left and right and left is not right and left.prev is not right:

            # if the values at left and right do not match, the list is not a palindrome
            if left.value != right.value:
                return False
            
            left = left.next    # move the left pointer to the next node
            right = right.prev  # move the right pointer to the previous node

        return True

# Start of the script
linked_list = DoublyLinkedList()

# read input values
values = [int(x) for x in input().split()]
for value in values:
    linked_list.insert_at_tail(value)

print(linked_list.is_palindrome())


# === Example Input/Output ===
# > 11 22 33 44
# False

# > 4 2 2 4
# True