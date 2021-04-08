"""
Author: Electra Bree
Assignment related to nodes
"""

class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next
        
    def __str__(self):
        return str(self.__data)
        
    def get_data(self):
        return self.__data
        
    def set_data(self, new_data):
        self.__data = new_data
    
    def get_next(self):
        return self.__next
        
    def set_next(self, new_next):
        self.__next = new_next
        
    def add_after(self, value):
        new_node = Node(value)
        temp_node = self.get_next()
        self.set_next(new_node)
        if self.__next != None:
            new_node.set_next(temp_node)
    def remove_after(self):
        remove_node = self.get_next()
        next_node = remove_node.get_next()
        remove_node.set_next(None)
        if next_node != None:
            self.set_next(next_node)
        else:
            self.set_next(None)

# Takes a Python list as a parameter and returns a reference to a linked chain of nodes.
def create_node_chain(values):
    first_node = Node(values[0])
    previous_node = None
    for index in range(1, len(values)):
        node = Node(values[index])
        if index == 1:
            previous_node = first_node
        previous_node.set_next(node)
        previous_node = node
    return first_node
        
# Takes a reference to a linked chain of nodes as a parameter and returns all the elements in the chain as a Python list
def convert_to_list(first_node):
    node_list = []
    current_node = first_node
    next_node = first_node.get_next()
    
    while current_node != None:
        node_list.append(current_node.get_data())
        current_node = next_node
        try:
            next_node = next_node.get_next()
        except:
            next_node = None
    return node_list

# Takes a Node object as a parameter and returns the number of nodes in this linked chain
def get_chain_length(first_node):
    nodes = 0
    
    current_node = first_node
    next_node = first_node.get_next()
    
    while current_node != None:
        nodes += 1
        current_node = next_node
        try:
            next_node = next_node.get_next()
        except:
            next_node = None
    return nodes

# Inserts nodes using data from the two parameter chain of nodes at alternate positions and returns a new linked chain of nodes
def merge_two_chains(chain1, chain2):
    node_list = []
    current_chain1 = chain1
    current_chain2 = chain2
    next_chain1 = current_chain1.get_next()
    next_chain2 = current_chain2.get_next()
    number = 1
    #Make a new list
    while current_chain2 != None:
        if number == 1:
            node_list.append(current_chain1.get_data())
            number = 2
            current_chain1 = next_chain1
            try:
                next_chain1 = next_chain1.get_next()
            except:
                next_chain1 = None
        else:
            node_list.append(current_chain2.get_data())
            number = 1
            current_chain2 = next_chain2
            try:
                next_chain2 = next_chain2.get_next()
            except:
                next_chain2 = None

    #Turn list into linked chain
    first_node = Node(node_list[0])
    previous_node = None
    for index in range(1, len(node_list)):
        node = Node(node_list[index])
        if index == 1:
            previous_node = first_node
        previous_node.set_next(node)
        previous_node = node
    return first_node


