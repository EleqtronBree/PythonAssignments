"""
Author: Electra Bree
Assignment related to binary search trees
"""

# Represents a binary search tree
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, left=self.__left)
            self.__left = t

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, right=self.__right)
            self.__right = t

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right
        
    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
    def insert(self, value):
        if value == self.get_data():
            print("Duplicate")
        else:
            if value < self.get_data():
                if self.get_left() == None:
                    self.set_left(BinarySearchTree(value))
                else:
                    self.get_left().insert(value)
            else:
                if self.get_right() == None:
                    self.set_right(BinarySearchTree(value))
                else:
                    self.get_right().insert(value)

# Creates a binary search tree
def create_bigger_bs_tree():
    root = BinarySearchTree(27)
    
    left = BinarySearchTree(14)
    lleft = BinarySearchTree(10)
    rleft = BinarySearchTree(19)
    
    right = BinarySearchTree(35)
    lright = BinarySearchTree(31)
    rright = BinarySearchTree(42)
    
    root.set_left(left)
    root.set_right(right)
    left.set_left(lleft)
    left.set_right(rleft)
    right.set_left(lright)
    right.set_right(rright)
    return root

# Inserts a node into a given binary search tree, given it doesn't already exist
def print_insert_position(bst, value):
    if value == bst.get_data():
        print("Duplicate")
    else:
        if value < bst.get_data():
            if bst.get_left() == None:
                print("To the left of {}".format(bst.get_data()))
            else:
                print_insert_position(bst.get_left(), value)
        else:
            if bst.get_right() == None:
                print("To the right of {}".format(bst.get_data()))
            else:
                print_insert_position(bst.get_right(), value)

# Traverses through the given binary search tree in-order
def traverse_bst_inorder(bst):
    if bst == None:
        return
    traverse_bst_inorder(bst.get_left())
    print(bst.get_data(), end = " ")
    traverse_bst_inorder(bst.get_right())

# Traverses through the given binary search tree pre-order
def traverse_bst_preorder(bst):
    if bst == None:
        return
    print(bst.get_data(), end = " ")
    traverse_bst_preorder(bst.get_left())
    traverse_bst_preorder(bst.get_right())
# Traverses through the given binary search tree post-order
def traverse_bst_postorder(bst):
    if bst == None:
        return
    traverse_bst_postorder(bst.get_left())
    traverse_bst_postorder(bst.get_right())
    print(bst.get_data(), end = " ")

# Returns the largest value in a given binary search tree
def get_maximum(bst):
    if not bst.get_right():
        return bst.get_data()
    return get_maximum(bst.get_right())

# Returns the smallest value in a given binary search tree
def get_minimum(bst):
    if not bst.get_left():
        return bst.get_data()
    return get_minimum(bst.get_left())

# Converts a binary search tree into a list in ascending order
def convert_to_list(bst, values):
    if not bst:
        return
    convert_to_list(bst.get_left(), values)
    values.append(bst.get_data())
    convert_to_list(bst.get_right(), values)
    return values

# Creates a balanced binary search tree from a given sorted list
def create_from_list(values):
    if len(values) == 0:
        return
    mid = len(values) // 2
    root = BinarySearchTree(values[mid])
    root.set_left(create_from_list(values[0:mid]))
    root.set_right(create_from_list(values[mid + 1:]))
    return root
