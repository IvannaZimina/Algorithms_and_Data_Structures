class HashData:
    # initialize a list of 10 items
    def __init__(self):
        self.size = 10                  # initial size of hash table
        self.table = [None] * self.size # hash table initialized with None
        self.lf_threshold = 0.7         # load factor threshold for resizing
        self.count = 0                  # how many slots are occupied

    # compute hash
    def hash_function(self, key):
        # key → hash_function → index
        # example: key = 25, size = 10 → index = 25 % 10 = 5
        return key % self.size

    # insert data to hash table
    def put(self, key):
        # call the hash function to compute the index for the given key
        index = self.hash_function(key)

        # conflict resolution
        # if the place is occupied, we need to find the next available slot
        while self.table[index] is not None:
            # move to the right along the array,
            # and if the end is reached, start again from the beginning
            # 5 → occupied
            # 6 → occupied
            # 7 → occupied
            # 8 → occupied
            # 9 → occupied
            # index = (9 + 1) % 10 = 0
            index = (index + 1) % self.size

        # insert the key into the hash table
        self.table[index] = key

        # increment the count of occupied slots
        self.count += 1

        # current load_factor = occupied slot/total slots
        # if load_factor > self.lf_threshold = 0.7: call rehash() to resize the table
        # calculate load factor
        lf = self.count / self.size

        # check if load factor exceeds after each insertion
        if lf > self.lf_threshold:
            print("Rehashing needed...")
            self.rehash()

    def rehash(self):
        # link to old table
        # example:
        # old_table → [None, None, 15, 25, None, ...]
        # self.table → [None, None, 15, 25, None, ...]
        # two variables point to the same list
        old_table = self.table

        # double the size of the hash table
        self.size *= 2

        # initialize new hash table with None
        self.table = [None] * self.size
        self.count = 0

        # insert old elements into the new table through the put() method
        for key in old_table:
            if key is not None:
                self.put(key)

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")

    #example:
    # self.table = [None, None, 15, None, 25]
    # hash_value = 0, key = None
    # hash_value = 1, key = None
    # hash_value = 2, key = 15
    # hash_value = 3, key = None
    # hash_value = 4, key = 25
    # ==== output ====
    # 0: None
    # 1: None
    # 2: 15
    # 3: None
    # 4: 25

if __name__ == "__main__":
    hash1 = HashData()

    # keys
    keys = [int(x) for x in input().split(', ')]

    # apply hash function to each key
    for key in keys:
        hash1.put(key)

    hash1.display()

# === input ===
# 34, 24, 35, 56, 2, 345, 46

# === output ===
# 0: None
# 1: None
# 2: 2
# 3: None
# 4: 34
# 5: 24
# 6: 35
# 7: 56
# 8: 345
# 9: 46