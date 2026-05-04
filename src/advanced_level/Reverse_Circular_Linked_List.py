# Replace # TODO: with your code

class Node:
    def __init__(self, data):
        """ 1. Define a Node class with:
            data: A value attribute to store data.
            next: A next pointer linking to the next node.
        """
        # A value attribute to store data.
        self.data = data
        # A next pointer linking to the next node.
        self.next = None

# circular linked list class to manage nodes
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ================== Helpers ==================

    # private helper to find the tail node (last node whose next points to head)
    # use in insert_at_head and insert_at_tail to find tail for linking, and in delete to link around removed head
    def _find_tail(self):
        # 3.3. if list is empty, return None
        if not self.head:
            return None

        node = self.head

        # walk until node.next points back to head
        while node.next is not self.head:
            node = node.next
        return node

    # helper: return True if list has exactly one node
    # use in delete and insert methods to check if deals with a single-node list
    def _is_single(self):
        return bool(self.head and self.head.next is self.head)

    # helper: set list to a single node (node.next -> node) and set head
    # use in insert_at_head and insert_at_tail when list is empty to initialize the list
    def _set_single_node(self, node: Node):
        self.head = node
        node.next = node
        return True

    # helper: get node at position (0-based). return None if out of bounds
    # use in insert_node and delete_node to find nodes by position
    def _get_node_at(self, position: int):
        # 3.3. check for empty list or invalid position
        if not self.head or position < 0:
            return None

        node = self.head
        idx = 0

        # walk through the list until the desired position is reached or come back to head
        while idx < position:
            node = node.next
            # if a full circle complete, position is out of bounds
            if node is self.head:
                return None
            idx += 1
        return node
    
    # ==================== Mock and Display Methods ====================

    # helper: create a mock circular linked list with 4 nodes (90->80->60->50->90) and set head to node 90
    def create_mock_linked_list(self):
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        # link nodes in order: node1 -> node2 -> node3 -> node4
        node1.next = node2
        node2.next = node3
        node3.next = node4
        # close the circle: last node points back to first
        node4.next = node1

        # set head of the list to first node
        self.head = node1

    def display(self):
        if not self.head:
            print('None')
            return

        parts = []
        node = self.head
        parts.append(str(node.data))
        node = node.next
        while node is not self.head:
            parts.append(str(node.data))
            node = node.next

        # show that it returns to head
        parts.append(str(self.head.data))
        print('->'.join(parts))
    
    # ================== Main Methods ==================

    # 2.1. insert new node at the beginning (head)
    def insert_at_head(self, value):
        # make new node
        new_node = Node(value)

        # if list empty, initialize single-node list
        if not self.head:
            return self._set_single_node(new_node)

        # find last node to link it to new head using helper
        tail = self._find_tail()

        # insert new node before current head
        new_node.next = self.head

        # link tail to new head
        tail.next = new_node

        # update head to new node
        self.head = new_node
        return True

    # 2.2. Insert a new node at the end.
    def insert_at_tail(self, value):
        # create new node with value and add to end
        new_node = Node(value)

        # if list empty, initialize single-node list
        if not self.head:
            return self._set_single_node(new_node)

        # find tail and attach new node using helper
        tail = self._find_tail()

        # link tail to new node and new node back to head
        tail.next = new_node

        # link new node back to head to maintain circle
        new_node.next = self.head
        return True

    # 2.3. Remove a node with the given value.
    def delete(self, value):
        # if list empty, nothing to do
        if not self.head:
            return False

        # if head holds the value
        if self.head.data == value:
            # then if head is the only node, just remove it
            if self._is_single():
                self.head = None
                return True

            # find tail and link around removed head using helper
            tail = self._find_tail()

            # remove head by moving head forward and fixing tail
            self.head = self.head.next

            # link tail to new head to maintain circle
            tail.next = self.head
            return True

        # prev points to node before the one to check (start at head)
        prev = self.head

        # curr is the node that will check next (node after head)
        curr = self.head.next
        
        # loop until we come back to head
        while curr is not self.head:
            if curr.data == value:
                # skip the current node
                prev.next = curr.next
                return True

            # move prev and curr forward
            prev = curr
            curr = curr.next

        return False

    # This method reverses a circular linked list in place.
    def reverse(self):
        # if list is empty or has only one node, no need to reverse
        if not self.head or self.head.next is self.head:
            return

        prev = self.head        # prev is the previous node; start at the head.
        curr = self.head.next   # curr is the current node, following the head.

        # loop until come back to head, reversing the next pointers
        while curr is not self.head:
            nxt = curr.next     # Save the next node to avoid losing the connection.
            curr.next = prev    # Reverse the edge: the current node now points backward.
            prev = curr         # Move prev forward to the current node.
            curr = nxt          # Move to the next node (which was saved).

        self.head.next = prev   # After the loop, prev is the former tail.
        self.head = prev        # Update the head to the new one (the former tail).


# Start of the script
linked_list = CircularLinkedList()

# read input keys
values = [int(x) for x in input().split()]
for value in values:
    linked_list.insert_at_tail(value)

linked_list.reverse()
linked_list.display()

# ==== Expected Input/Output ====
# Input: 10 20 30 40
# Output: 40->30->20->10->40

# Input: 11 22 33 44
# Output: 44->33->22->11->44