# Replace # TODO: with your code

class Node:
    def __init__(self, data):
        """Simple node for doubly linked list.

        Attributes:
            data: value stored in node
            next: pointer to next node
            prev: pointer to previous node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        """Initialize empty list with head and tail."""
        self.head = None
        self.tail = None

    # ================== Helpers ==================

    # helper: set list to a single node
    # use in insert_at_head and insert_at_tail when list is empty to initialize the list
    def _set_single_node(self, node: Node):
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        return True

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
            return
        
        # walk through the list and collect data for string representation
        parts = []

        # asign to a variable to avoid modifying self.head while walking
        node = self.head

        # walk through the list until the end is reached (node is None)
        while node:
            parts.append(str(node.data))
            node = node.next

        # join parts with <-> to show links between nodes
        print('<->'.join(parts))

    # 2.4. Print the list from tail to head. Format: `C<->B<->A` or `None` if empty.
    def display_backward(self):
        # 3.3. check for empty list
        if not self.tail:
            print('None')
            return
        
        # walk through the list and collect data for string representation
        parts = []

        # asign to a variable to avoid modifying self.tail while walking
        node = self.tail

        # walk through the list until the beginning is reached (node is None)
        while node:
            parts.append(str(node.data))
            node = node.prev

        # join parts with <-> to show links between nodes
        print('<->'.join(parts))

    # ================== Main Methods ==================

    # 2.1. insert new node at the beginning (head)
    def insert_at_head(self, value):
        # make new node
        new_node = Node(value)

        # if list empty, initialize single-node list
        if not self.head:
            return self._set_single_node(new_node)
        
        # link new node before current head
        new_node.next = self.head

        # link current head back to new node
        self.head.prev = new_node

        # update head to new node
        self.head = new_node

        return True

    # 2.3. remove node by value
    def delete(self, value):
        # if list empty, nothing to do
        if not self.head:
            return False

        # asign to a variable to avoid modifying self.head while searching
        node = self.head

        # search for value in the list and stop when found or end of list reached
        while node and node.data != value:
            node = node.next

        # if node is None, value not found
        if not node:
            return False

        # remove the found node if node is head
        if node is self.head:
            # single node
            if self.head is self.tail:
                self.head = None
                self.tail = None
                return True
            # more than one node
            self.head = node.next
            self.head.prev = None
            node.next = None
            return True

        # if node is tail
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
        # node is in middle
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None
        return True

    # helper: remove a node object from the list (head/tail/middle)
    def _remove_node(self, node: Node):
        if node is None:
            return False
        # link previous
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        # link next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None
        return True

    # Simplified delete: find node and call helper
    def delete(self, value):
        if not self.head:
            return False
        node = self.head
        while node and node.data != value:
            node = node.next
        if not node:
            return False
        return self._remove_node(node)
