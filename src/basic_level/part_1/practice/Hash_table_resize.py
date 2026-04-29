class HashData:
    # initialize a list of 10 items
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.lf_threshold = 0.7

    # compute hash
    def hash_function(self, key):
        return key % self.size

    # insert data to hash table
    def put(self, key):
        # insert into table

        # compute threshold during each insertion
        # current lf = occupied slot/total slots

        # check if load factor exceeds after each insertion


    def rehash(self):
        # create a new hash table

        # hash existing data into new table

        # update table

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")


if __name__ == "__main__":
    hash1 = HashData()

    # keys
    keys = [int(x) for x in input().split(', ')]

    # apply hash function to each key
    for key in keys:
        hash1.put(key)

    hash1.display()
