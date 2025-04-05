class HashData:
    """
    A hash table implementation with linear probing for collision resolution
    """
    
    def __init__(self):
        """
        Initializes the hash table with 10 slots (None values)
        """
        # table size is set to 10 for simplicity
        self.table = [None] * 10  
    
    def hash_function(self, key):
        """
        A hash func which computes index based on given key
        
        Args:
            key (int): The key to hash
        
        Returns:
            int: Index in hash table where key will be stored
        """
        # use module by 10 as hash func 
        # to get an index in treshholds of table size
        return key % 10
    
    def put(self, key):
        """
        Inserts a key in hash table, if hash collision 
        (the computed index is already full),
        method will use linear probing to find next free slot
        
        Args:
            key (int): The key to be inserted into the hash table.
        """
        # calc hash value (index)
        hash_value = self.hash_function(key)  
        
        # linear probing to handle collision:
        # going through and keep checking next slots
        # until an empty one will be found
        while self.table[hash_value] is not None:
            # move to next slot (circular adding)
            hash_value = (hash_value + 1) % len(self.table)
        
        # insert the key in found empty slot
        self.table[hash_value] = key
    
    def display(self):
        """
        Displays the hash table with all his slots and showing each slot's value
        """
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value}")


keys = [int(x) for x in input("Enter keys (comma-separated): ").split(', ')]

hash1 = HashData()

for key in keys:
    hash1.put(key)

hash1.display()
