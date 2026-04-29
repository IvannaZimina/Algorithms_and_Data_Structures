class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return (key) % 10

    # insert data to hash table
    def put(self, key):
        while self.table[hash_value]:
            # move to next slot until empty space is found

        # insert into empty slot

    # display hash table
    def display(self):


# keys
keys = [int(x) for x in input().split(', ')]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()
