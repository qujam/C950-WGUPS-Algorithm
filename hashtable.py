# creating a hash table with insertion and lookup functions
class HashTable:
    # initialize the list of lists and set capacity to 10
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # initialize a hashing function to place packages in the correct buckets. key being package ID
    def hash_function(self, key):
        return hash(key) % self.capacity

    # create function to insert new package object into hash table
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_value].append((key, value))

    # create function to lookup package object in hash table
    def lookup(self, key):
        hash_value = self.hash_function(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                return pair[1]
        return None

    def __str__(self):
        output = "Hash Table Contents:\n"
        for i, bucket in enumerate(self.table):
            output += f"Bucket {i}: {bucket}\n"
        return output
    def __repr__(self):
        output = "Hash Table Contents:\n"
        for i, bucket in enumerate(self.table):
            output += f"Bucket {i}: {bucket}\n"
        return output