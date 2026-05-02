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

    # helper: set list to a single node
    def _set_single_node(self, node: Node):
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        return True

    # helper: return forward string like "A<->B<->C" or "None"
    def _to_str_forward(self):
        if not self.head:
            return 'None'
        parts = []
        node = self.head
        while node:
            parts.append(str(node.data))
            node = node.next
        return '<->'.join(parts)

    # helper: return backward string from tail to head
    def _to_str_backward(self):
        if not self.tail:
            return 'None'
        parts = []
        node = self.tail
        while node:
            parts.append(str(node.data))
            node = node.prev
        return '<->'.join(parts)

    # 3.1. Insert multiple elements and verify bidirectional traversal: 90<->80<->60<->50
    def create_mock_linked_list(self):
        """Create a sample list: 90 <-> 80 <-> 60 <-> 50"""
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

    # 2.4. Display: print insertion result, delete node 90, then print result after deletion
    def display(self):
        """Print forward representation, remove node 90 and show result."""
        insertion = self._to_str_forward()
        print('1. Inserting multiple elements and verifying bidirectional traversal:', insertion)

        # delete node with value 90 and report
        deleted = self.delete(90)
        print('Node 90 deleted' if deleted else 'Node 90 not found')

        # print list after deletion and check backward traversal
        after = self._to_str_forward()
        backward = self._to_str_backward()
        # check bidirectional links: forward reversed equals backward
        forward_parts = after.split('<->') if after != 'None' else []
        backward_parts = backward.split('<->') if backward != 'None' else []
        bidir_ok = (not forward_parts and not backward_parts) or (forward_parts[::-1] == backward_parts)
        print('2. Deleting nodes and checking if the bidirectional property remains intact:', f"{after}", f"(deleted={deleted}, bidirectional={bidir_ok})")

    # 2.1. insert new node at the beginning (head)
    def insert_at_head(self, value):
        """Insert value at head. Return True on success."""
        new_node = Node(value)
        if not self.head:
            return self._set_single_node(new_node)
        # link new node before current head
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return True

    # 2.2. insert new node at the end (tail)
    def insert_at_tail(self, value):
        """Insert value at tail. Return True on success."""
        new_node = Node(value)
        if not self.tail:
            return self._set_single_node(new_node)
        # link after current tail
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return True

    # 2.3. remove node by value
    def delete(self, value):
        """Delete first node with matching value. Return True if removed."""
        if not self.head:
            return False

        node = self.head
        # search for value
        while node and node.data != value:
            node = node.next

        if not node:
            return False

        # if node is head
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
            node.prev = None
            return True

        # node is in middle
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None
        return True

# Start of the script
linked_list = DoublyLinkedList()

# create the initial linked list
linked_list.create_mock_linked_list()

# print the updated linked list
linked_list.display()
