# a class to represent a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# a class to represent a linked list


class LinkedList:
    def __init__(self):
        self.head = None

    # return the linked list elements
    def traverse(self):
        current = self.head

        result = ""

        while current:
            result += (f"{current.data}->")
            current = current.next

        result += "None"

        return result

    # append an item to the linked list
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


class HashData:
    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return key % 10

    # insert data to hash table
    def put(self, key):
        # insert into table
        
        # if the slot is empty
        
            # create a linked list at the slot
        
        # append item to the linked list
        

    # display hash table
    def display(self):
        
            # if slot is a linked list

            # if slot is empty



hash1 = HashData()

# keys
keys = [int(x) for x in input().split(', ')]

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()
