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

    # another variant of traverse method, which returns a list of elements in the linked list
    # def traverse(self):
    #     current = self.head
    #     result = []

    #     while current:
    #         result.append(str(current.data))
    #         current = current.next

    #     return "->".join(result) + "->None"


    # append an item to the linked list
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        # find the last node which is not None
        while current.next:
            current = current.next
        # after that the current node is the last node, so we can append the new node to it
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
        # example: if key = 5, then calculate 25%10 = 5,
        # so put the item in the slot with index 5
        index = self.hash_function(key)

        # if the slot is empty - create a linked list at the slot
        if self.table[index] is None:
            self.table[index] = LinkedList()

        # append item to the linked list
        self.table[index].append(key)

    # display hash table
    def display(self):
            
        for i, slot in enumerate(self.table):
            if slot is None:
                print(f"{i}: None")
            else:
                print(f"{i}: {slot.traverse()}")

        # for hash_value, slot in enumerate(self.table):
        #   # if slot is a linked list
        #   # from the put() method we know, that if the slot can be None or LinkedList, and no any other type, so check (isinstance) is not necessary
        #   if isinstance(slot, LinkedList):
        #       print(f"{hash_value}: {slot.traverse()}")
        #   # if slot is empty
        #   else:
        #       print(f"{hash_value}: None")

hash1 = HashData()

# keys
keys = [int(x) for x in input().split(', ')]

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()

# ===== input =====
# 10, 34, 35, 6, 90, 33

# ===== output =====
# 0: 10->90->None
# 1: None
# 2: None
# 3: 33->None
# 4: 34->None
# 5: 35->None
# 6: 6->None
# 7: None
# 8: None
# 9: None