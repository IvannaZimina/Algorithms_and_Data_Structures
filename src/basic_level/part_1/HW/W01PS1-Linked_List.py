# Replace # TODO: with your code

class Node:
    def __init__(self, data):
        """_summary_

        Args:
            data (_type_): _description_
        """
        # TODO:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """_summary_
        """
        self.head = None

    # create the linked list: 90->80->60->50
    def create_mock_linked_list(self):
        """_summary_
        """
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

    # display linked list in format: A->B->C
    def display(self):
        """_summary_
        """
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # method to append a node
    def append(self, data):
        # create new node with the given data
        new_node = Node(data)

        # If the list has no head, the new node becomes the head (so the list now has one node).
        if self.head is None:
            self.head = new_node
            return

        # Move to the last node to attach the new node.
        current = self.head

        # traverse through the list until the last element is reached
        while current.next:
            current = current.next
        
        # finally, append the new node at the end of the linked list
        current.next = new_node

    # insert node to linked list
    def insert_node(self, data, position: int):
        """_summary_

        Args:
            data (_type_): _description_
            position (_type_): _description_
        """
        new_node = Node(data)

        # if the position is 0, new element becomes the new head of the linked list and the old head becomes the next element of the new head
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # start from the head of the list
        current = self.head

        # traverse to the position where the new node will be inserted
        for _ in range(position - 1):
            # if current becomes None, position is invalid
            if current is None:
                raise IndexError("Position out of bounds")
            #  move to the next node
            current = current.next

        # new node points to the next node of current
        new_node.next = current.next

        # current now points to the new node
        current.next = new_node

    # method to delete node at the given position
    def delete_node(self, position: int):
        """_summary_

        Args:
            position (int): _description_
        """
        # if the linked list is empty, print a message and return
        if self.head is None:
            print("List is empty")
            return

        # if position is 0, remove the first node (head)
        if position == 0:
            # self.head.next (position) equals None
            # self.head becoms None
            # list becomes empty
            self.head = self.head.next
            return

        # start from the head of the list
        current = self.head

        # index counter to track current position
        index = 0

        # traverse to the node just before the one we want to delete
        while current.next and index < position - 1:
            current = current.next
            index += 1

        # if current.next is None, it means the position is out of range
        if current.next is None:
            print("Position out of range")
            return

        # skip the node to be deleted by changing the link
        current.next = current.next.next

# Start of the script
linked_list = LinkedList()

# create the initial linked list
linked_list.create_mock_linked_list()

# print the updated linked list
linked_list.display()
