class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return (key) % 10

    # insert data to hash table
    def put(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            # move to next slot until empty space is found
            hash_value = (hash_value + 1) % len(self.table)

        # insert into empty slot
        self.table[hash_value] = key

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")


# keys
keys = [int(x) for x in input().split(', ')]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()
