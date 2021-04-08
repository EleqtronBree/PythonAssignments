"""
Author: Electra Bree
Assignment related to hash tables
"""

class SimpleHashTable:
    def __init__(self, size=13):
        self.__size = size
        self.__slots = [None] * size

    def put(self, string_and_key_tuple):
        hash_value = self.get_hash_value(string_and_key_tuple)
        index = hash_value % self.__size
        self.__slots[index] = string_and_key_tuple
        

    def get_hash_value(self,string_and_key_tuple):
        return string_and_key_tuple[1]

    def __str__(self):
        return str(self.__slots)

class DoubleHashTable:
    def __init__(self, size=13, q=11):
        self.__size = size
        self.__slots = [None] * size
        self.__q = q

    def put(self,key):
        original_hash_value = self.get_hash_value(key)
        hash_value = original_hash_value
        step = 0
        while self.__slots[hash_value] != None:
            step += 1
            second_hash_value  = self.get_second_hash_value(key)
            hash_value = (original_hash_value + step * second_hash_value) % self.__size
        self.__slots[hash_value] = key

    def get_hash_value(self, key):
        return key % self.__size

    def get_second_hash_value(self, key):
        return self.__q - (key % self.__q)

    def __str__(self):
        return str(self.__slots)

class QuadraticHashTable:
    def __init__(self, size=13):
        self.__size = size
        self.__slots = [None] * size

    def put(self, key):
        original_index = key % self.__size
        index = original_index
        step = 1
        while self.__slots[index] != None:
            index = self.rehash(original_index, step)
            step += 1
        self.__slots[index] = key

    def get_hash_value(self, key):
        return key % self.__size

    def rehash(self, old_hash, distance):
        return (old_hash + distance ** 2) % self.__size

    def __str__(self):
        return str(self.__slots)

class SimpleChainHashTable:
    def __init__(self, size=13):
        self.__size = size
        self.__slots = [[] for item in range(size)]
    def get_hash_value(self, key):
        return key % self.__size
        
    def __str__(self):
        return "{}".format(self.__slots)
        
    def put(self, key):
        index = self.get_hash_value(key)
        self.__slots[index].append(key)
        
    def __len__(self):
        sum_elements = 0
        for sublist in self.__slots:
            for element in sublist:
                sum_elements += 1
        return sum_elements

# Computes the hash value of the key using the mid-square method and returns it
def get_simple_numeric_hash(key, table_size):
    n = key ** 2
    n = int(str(n)[1:-1])
    n = n % table_size
    return n

# Returns the sum of ASCII codes of characters in the key
def get_simple_hash(key, table_size):
    key_sum = 0
    for letter in key:
        key_sum += ord(letter)
    return key_sum % table_size

# Takes a key to be inserted and the hashtable (python list), and inserts the key into the hashtable using the primary hash function
def hash_linear(key, table):
    hash_index = key % len(table)
    step = 0
    probe = 1
    while table[hash_index] != None:
        probe += 1
        step += 1
        hash_index = (key + step) % len(table)
    table[hash_index] = key
    return (probe, table)

# Takes a key to be inserted and the hashtable (python list), and inserts the key into the hashtable using the secondary hash function
def hash_double(key, table):
    hash_index = key % len(table)
    hash_step = 5 - (key % 5)
    probe = 1
    while table[hash_index] != None:
        probe += 1
        hash_index = (hash_index + hash_step) % len(table)
    table[hash_index] = key
    return (probe, table)

# Takes a key to be inserted and the hashtable (python list), and inserts the key into the hashtable using the quadractic hash function
def hash_quadratic(key, table):
    hash_index = key % len(table)
    step = 0
    probe = 1
    while table[hash_index] != None:
        probe += 1
        step += 1
        hash_index = (key + step ** 2) % len(table)
    table[hash_index] = key
    return (probe, table)

