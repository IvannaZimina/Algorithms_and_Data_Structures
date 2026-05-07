# Replace # TODO: with your code

class Node:
    def __init__(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        # TODO:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """_summary_
        """
        self.head = None

    # display linked list in format: A->B->C
    def display(self):
        """_summary_
        """
        current = self.head
        while current:
            print(f"{current.value}", end="->")
            current = current.next
        print(None)

    # Insert a new node at the end.
    def insert_at_tail(self, value):
        # create new node with the given data
        new_node = Node(value)

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

    # Insert a new node at the beginning.
    def insert_at_head(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        # create new node with the given data
        new_node = Node(value)

        # assign new node's next to current head
        new_node.next = self.head
        # update head to new node
        self.head = new_node

    # method to delete node with the given value
    def delete(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        # if the linked list is empty, print a message and return
        if self.head is None:
            print("List is empty")
            return

        # if the head node matches, remove the first node (head)
        if self.head.value == value:
            # self.head.next equals None
            # self.head becomes None
            # list becomes empty
            self.head = self.head.next
            return

        # start from the head of the list
        previous = self.head
        current = self.head.next

        # traverse to the node just before the one we want to delete
        while current:
            if current.value == value:
                # skip the node to be deleted by changing the link
                previous.next = current.next
                return
            previous = current
            current = current.next

        # if current is None, it means the value is not in the list
        print("Value not found")

if __name__ == "__main__":
    # Start of the script
    linked_list = LinkedList()

    # create the initial linked list
    linked_list.insert_at_head(80)
    linked_list.insert_at_head(90)
    linked_list.insert_at_tail(60)
    linked_list.insert_at_tail(50)

    # print the updated linked list
    linked_list.display()

    # delete specific elements and check correctness
    linked_list.delete(90)
    linked_list.display()

    # edge case: value not found
    linked_list.delete(999)
    linked_list.display()

# ================ Expected Output: ================

# 90->80->60->50->None
# 80->60->50->None
# Value not found
# 80->60->50->None