"""
Author: Electra Bree
Assignment related to queues
"""

class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop() 

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[len(self.__items)-1]

    def __str__(self):
        return 'Queue: ' + str(self.__items[::-1])
        
    def enqueue_list(self, a_list):
        for element in a_list:
            self.enqueue(element)

# Takes a positive integer as a parameter. The function creates and returns a new queue,
# where the front of the queue is the parameter value n, and all subsequent values in the queue decrease by 1 until the rear of the queue has the value equal to 1
def countup_queue(number):
    queue = Queue()
    for element in range(number, 0, -1):
        queue.enqueue(element)
    return queue

# Takes a Queue as a parameter, and returns the value that is at the front of the queue
def get_front_of_queue(a_queue):
    if a_queue.size() == 0:
        return None
    else:
        return a_queue.peek()

# Exchanges the elements of the first queue and the second queue
def exchange_queue(queue1, queue2):
    temp_queue = Queue()
    for element in range(queue1.size()):
        temp_queue.enqueue(queue1.dequeue())
    for element in range(queue2.size()):
        queue1.enqueue(queue2.dequeue())
    for element in range(temp_queue.size()):
        queue2.enqueue(temp_queue.dequeue())

# Modifies the parameter Queue object so that the original queue items appear in their original order followed by a copy of the queue items in reverse order
def mirror_queue(a_queue):
    stack = Stack()
    temp_queue = Queue()
    size = a_queue.size()
    for number in range(size):
        element = a_queue.dequeue()
        stack.push(element)
        temp_queue.enqueue(element)
    for number in range(size):
        a_queue.enqueue(temp_queue.dequeue())
    for number in range(size):
        a_queue.enqueue(stack.pop())
