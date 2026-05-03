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

    # helper: convert list to string starting from a node and following a direction (next or prev)
    # use in display methods to create string representation of the list
    def _to_str(self, start_node, direction_attr):
        if not start_node:
            return 'None'

        # list to hold string parts for joining
        parts = []
        node = start_node
        while node:
            parts.append(str(node.value))
            node = getattr(node, direction_attr)
        return '<->'.join(parts)

    # =================== Mock and Display Methods ===================

    # 3.1. Insert multiple elements and verify bidirectional traversal: 90<->80<->60<->50
    def create_mock_linked_list(self):
        n1 = Node(90)
        n2 = Node(80)
        n3 = Node(60)
        n4 = Node(50)

        # link nodes forward and backward
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3

        # set head and tail
        self.head = n1
        self.tail = n4

    # 2.3. Print the list from head to tail. Format: `A<->B<->C` or `None` if empty.
    def display_forward(self):
        # 3.3. check for empty list
        if not self.head:
            print('None')
            return False

        print(self._to_str(self.head, 'next'))

        # 3.2. Delete nodes (ex. node 60) and check if bidirectional links remain intact.
        deleted = self.delete(60)
        print('Node 60 deleted' if deleted else 'Node 60 not found')

        # check for empty list after deletion
        if not self.head:
            print('None')
            return False

        print(self._to_str(self.head, 'next'))
        return True

    # 2.4. Print the list from tail to head. Format: `C<->B<->A` or `None` if empty.
    def display_backward(self):
        # 3.3. check for empty list
        if not self.tail:
            print('None')
            return False

        print(self._to_str(self.tail, 'prev'))

        # 3.2. Delete nodes (ex. node 80) and check if bidirectional links remain intact.
        deleted = self.delete(80)
        print('Node 80 deleted' if deleted else 'Node 80 not found')

        # check for empty list after deletion
        if not self.tail:
            print('None')
            return False

        print(self._to_str(self.tail, 'prev'))
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

# Start of the script
linked_list = DoublyLinkedList()

# create the initial linked list
linked_list.create_mock_linked_list()

# Print the list from head to tail.
print('Forward (head to tail):')
linked_list.display_forward()

# Print the list from tail to head.
print('Backward (tail to head):')
linked_list.display_backward()

# ================ Expected Output: ================
# Forward (head to tail):
# 90<->80<->60<->50
# Node 60 deleted
# 90<->80<->50
# Backward (tail to head):
# 50<->80<->90
# Node 80 deleted
# 50<->90
