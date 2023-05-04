class Node:
    def __init__(self, data = None):
        self.data = data
        self.next_node = None

class HashTable:
    def __init__(self, size = None):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def hash_func(self, key, size):
        return key % size
        
    def insert(self, key, data):
        index = self.hash_func(key, self.size)
        self.slots[index] = key
        self.data[index] = data

    def get_data(self, key):
        index = self.hash_func(key, self.size)
        return self.data[index]
        # for i in self.slots:
        #     if i == key:
        #         print(self.data[i])

    def print_hash(self):
        print(list(zip(self.data, self.slots)))


table = HashTable(10)
table.insert(1, "a")
table.insert(2, "b")
print(table.get_data(21))
table.print_hash()