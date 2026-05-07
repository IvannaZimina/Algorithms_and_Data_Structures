# Replace # TODO: with your code

class Node:
    def __init__(self, value):
        """ 1. Define a Node class with:
            value: A value attribute to store data.
            next: A next pointer linking to the next node.
        """
        # A value attribute to store data.
        self.value = value
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

    # ==================== Mock and Display Methods ====================

    # helper: return string representation of list like "A->B->C->A" or "None"
    def _to_str(self):
        if not self.head:
            return 'None'

        parts = []
        node = self.head
        parts.append(str(node.value))
        node = node.next
        while node is not self.head:
            parts.append(str(node.value))
            node = node.next

        # show that it returns to head
        parts.append(str(self.head.value))
        return '->'.join(parts)

    # helper: create a mock circular linked list with 4 nodes (90->80->60->50->90) and set head to node 90
    def create_mock_linked_list(self):
        """_summary_
        """
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

    # 2.4. Print all elements in the list, looping back to the head if necessary: A->B->C->A
    def display(self):
        """_summary_
        """
        # print elements in order and show that it loops back to head
        insertion = self._to_str()
        print('Circular linked list:', insertion)
    
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
        if self.head.value == value:
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
            if curr.value == value:
                # skip the current node
                prev.next = curr.next
                return True

            # move prev and curr forward
            prev = curr
            curr = curr.next

        return False


# Start of the script
linked_list = CircularLinkedList()

# 3.1. Insert multiple elements and verify circular linkage.
linked_list.insert_at_head(80)
linked_list.insert_at_head(90)
linked_list.insert_at_tail(60)
linked_list.insert_at_tail(50)
linked_list.display()

# 3.2. Delete nodes and check if the circular property remains intact.
deleted = linked_list.delete(90)
print('Node 90 deleted' if deleted else 'Node 90 not found')
linked_list.display()

# 3.3. Handle edge cases: empty list and deleting the only node.
empty_list = CircularLinkedList()
deleted_empty = empty_list.delete(1)
print('Delete from empty list:', 'Success' if deleted_empty else 'Not found')

single_list = CircularLinkedList()
single_list.insert_at_head(10)
single_list.display()
deleted_single = single_list.delete(10)
print('Delete only node:', 'Success' if deleted_single else 'Not found')
single_list.display()

# ================ Expected Output: ================
# Circular linked list: 90->80->60->50->90
# Node 90 deleted
# Circular linked list: 80->60->50->80
# Delete from empty list: Not found
# Circular linked list: 10->10
# Delete only node: Success
# Circular linked list: None