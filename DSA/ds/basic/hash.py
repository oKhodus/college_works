class HashData:
    # initialize a list of 10 items
    def __init__(self):
        """A class implementing a hash table with open addressing and dynamic resizing"""
        # current size of the hash table (default is 10)
        self.size = 10
        # fixed size ls containing table elems
        self.table = [None] * self.size
        # load factor threshold, after which will be rehashing (default is 0.7)
        self.lf_threshold = 0.7
        # current num of elems in hash table
        self.count = 0

    # compute hash
    def hash_function(self, key) -> int:
        """Computes the hash index for a given key using the modulo operation"""
        return key % self.size

    # insert data to hash table
    def put(self, key) -> None:
        """Inserts a key into the hash table"""
        # Increment the counter for inserted elements
        self.count += 1
        # check if the load factor MORE THAN threshold
        if self.count / self.size >= self.lf_threshold:
            # if the threshold is less, need rehash method to resize the table
            self.rehash()

        index = self.hash_function(key)
        # insert into table
        if self.table[index] is None:
            # if the cell is empty - insert the key there
            self.table[index] = key
        else:
            while self.table[index]:
                # if the cell is full - start linear probing
                index = (index + 1) % self.size
            # if an empty cell is found - insert the key
            self.table[index] = key
        # compute threshold during each insertion
        # current lf = occupied slot/total slots

        # check if load factor exceeds after each insertion


    def rehash(self):
        # create a new hash table
        self.size = self.size * 2
        old_table = self.table
        self.table = [None] * self.size
        # hash existing data into new table
        for key in old_table:
            if key is not None:
                self.put(key)
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
