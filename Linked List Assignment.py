"""
Author: Electra Bree
Assignment related to linked lists
"""

class LinkedList:
    def __init__(self, head=None):
        self.__head = head
    
    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.__head)
        self.__head = new_node
    
    def is_empty(self):
        return self.__head == None

    def size(self):
        count = 0
        curr = self.__head
        while curr != None:
            count += 1
            curr = curr.get_next()
        return count
    
    def __str__(self):
        curr = self.__head
        string = "["
        while curr != None:
            if curr.get_next() != None:
                string = string + str(curr.get_data()) + ", "
            else:
                string = string + str(curr.get_data())
            curr = curr.get_next()
        string = string + "]"
        return string

    def remove_from_tail(self):
        curr = self.__head
        previous = None
        removed = None
        if curr.get_next() != None:
            while curr.get_next() != None:
                previous = curr
                curr = curr.get_next()
            previous.set_next(None)
        else:
            curr.set_next(None)
        removed = curr
        return removed
    
    def remove_from_head(self):
        removed = self.__head
        self.__head = self.__head.get_next()
        return removed
    
    def add_all(self, a_list):
        for element in a_list:
            self.add(element)
            
    def to_list(self):
        a_list = []
        curr = self.__head
        while curr != None:
            a_list.append(curr.get_data())
            curr = curr.get_next()
        return a_list
    
    def no_duplicate(self):
        duplicates = []
        curr = self.__head
        while curr != None:
            if curr.get_data() in duplicates:
                return False
            else:
                duplicates.append(curr.get_data())
            curr = curr.get_next()
        return True
        
    def search(self, search_value):
        found = False
        curr = self.__head
        previous = None
        while curr != None:
            if curr.get_data() == search_value:
                return True
            prevous = curr
            curr = curr.get_next()
        return False

class MyNumberIterator:
    def __init__(self, upper_limit):
        self.__upper_limit = upper_limit
        self.__current_number = 0
    
    def __next__(self):
        if self.__current_number == self.__upper_limit:
            raise StopIteration()
        self.__current_number = self.__current_number + 1
        return self.__current_number

class MyNumber:
    def __init__(self, upper_limit):
        self.__upper_limit = upper_limit
    
    def __iter__(self):
        return MyNumberIterator(self.__upper_limit)

class LinkedListIterator:
    def __init__(self, head):
        self.__current = head
        
    def __next__(self):
        if self.__current == None:
            raise StopIteration()
        curr = self.__current
        self.__current = self.__current.get_next()
        return curr
