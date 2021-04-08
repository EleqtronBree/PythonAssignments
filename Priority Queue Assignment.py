"""
Author: Electra Bree
Assignment related to priority queues
"""

# Represents a priority queue
class PriorityQueue:
    def __init__(self):
        self.__bin_heap = [0]
        self.__size = 0

    def insert(self, item):
        self.__bin_heap.append(item)
        self.__size += 1
        self.perc_up(self.__size)

    def __str__(self):
        return str(self.__bin_heap)

    def perc_up(self, i):
        #as long as parent exists
        while i // 2 > 0:
            #if child is less than parent node
            if self.__bin_heap[i] < self.__bin_heap[i // 2]:
                self.__bin_heap[i], self.__bin_heap[i // 2] = self.__bin_heap[i // 2],  self.__bin_heap[i]
            i = i // 2 #work upwards

    def get_min_child_index(self, i):
        if i * 2 + 1 > self.__size:
            return i * 2
        else:
            if self.__bin_heap[i * 2]  > self.__bin_heap[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def perc_down(self, i):
        while i * 2 <= self.__size: #child is within range
            min_child = self.get_min_child_index(i)
            #parent is greater
            if self.__bin_heap[i] > self.__bin_heap[min_child]:
                self.__bin_heap[i], self.__bin_heap[min_child] = self.__bin_heap[min_child], self.__bin_heap[i]
            i = min_child
    
    def del_min(self):
        return_val = self.__bin_heap[1]
        self.__bin_heap[1] = self.__bin_heap[self.__size]
        self.__size = self.__size - 1
        self.__bin_heap.pop()
        self.perc_down(1)
        return return_val
        
    def create_heap_fast(self, values):
        self.__bin_heap += values
        self.__size = len(values)
        for index in range(self.__size // 2, 0, -1):
            child = self.get_min_child_index(index)
            if self.__bin_heap[child] < self.__bin_heap[index]:
                self.__bin_heap[child], self.__bin_heap[index] = self.__bin_heap[index], self.__bin_heap[child]
        self.perc_down(1)
        self.perc_up(self.__size)

# Returns true if a given list is a valid binary heap
def is_binary_heap(values):
    for index in range(1, len(values)):
        lchild = 2 * index
        rchild = lchild + 1
        #check if these indices exist
        if lchild < len(values) and rchild < len(values):
            #if either children is less than its parent
            if values[lchild] < values[index] or values[rchild] < values[index]:
                return False
        elif lchild < len(values):
            if values[lchild] < values[index]:
                return False
        elif rchild < len(values):
            if values[rchild] < values[index]:
                return False
    return True

# Takes a list and creates a binary heap using a priority queue
def create_heap(values):
    priority_queue = PriorityQueue()
    for value in values:
        priority_queue.insert(value)
    return priority_queue

# Returns a list of values in ascending order using a priority queue
def heap_sort(values):
    sorted_list = []
    priority_queue = PriorityQueue()
    for value in values:
        priority_queue.insert(value)
    for index in range(1, len(values) + 1):
        min_child = priority_queue.del_min()
        sorted_list.append(min_child)
    return sorted_list
