"""
Author: Electra Bree
Assignment related to binary trees
"""

# Creates a binary tree
def create_a_tree():
    root = BinaryTree(7)
    root.insert_left(2)
    root.insert_right(9)
    left = root.get_left()
    left.insert_left(1)
    left.insert_right(5)
    right = root.get_right()
    right.insert_right(14)
    return root

def create_a_bigger_tree():
    root = BinaryTree("a")
    root.insert_left("b")
    root.insert_right("c")
    left = root.get_left()
    left.insert_left("d")
    left.insert_right("e")
    d = left.get_left()
    d.insert_right("f")
    e = left.get_right()
    e.insert_right("g")
    return root

# Takes a binary tree and prints the elements of a binary tree in preorder
def basic_print(b_tree):
    if b_tree == None:
        return
    print(b_tree.get_data(), end = " ")
    basic_print(b_tree.get_left())
    basic_print(b_tree.get_right())

# Takes a binary tree and returns the number of nodes
def count_nodes(b_tree):
    count = 0
    if b_tree == None:
        return 0
    else:
        count += 1
        return count + count_nodes(b_tree.get_left()) + count_nodes(b_tree.get_right())

# Takes a binary tree and returns a sum of all the nodes
def get_sum(b_tree):
    if b_tree == None:
        return 0 
    else:
        return b_tree.get_data() + get_sum(b_tree.get_left()) + get_sum(b_tree.get_right())

# Takes a binary tree and returns the depth
def get_tree_depth(b_tree):
    left_depth = 0
    right_depth = 0
    if b_tree.get_left() == None and b_tree.get_right() == None:
        return 0
    else:
        if b_tree.get_left() != None:
            left_depth += get_tree_depth(b_tree.get_left())
        if b_tree.get_right() != None:
            right_depth += get_tree_depth(b_tree.get_right())
        return 1 + max(left_depth, right_depth)

# Takes a binary tree and returns the sum of all leaf nodes
def get_sum_leaf_nodes(my_tree):
    if my_tree.get_left() == None and my_tree.get_right() == None:
        return my_tree.get_data()
    else:
        left_sum = 0
        right_sum = 0
        if my_tree.get_left() != None:
            left_sum += get_sum_leaf_nodes(my_tree.get_left()) 
        if my_tree.get_right() != None:
            right_sum += get_sum_leaf_nodes(my_tree.get_right())
        return left_sum + right_sum

# Takes a binary tree and returns true if all node values are even
def no_odds(my_tree):
    if my_tree.get_right() == None and my_tree.get_left() == None:
        if my_tree.get_data() % 2 != 0:
            return False
        return True
    else:
        left_logic = True
        right_logic = True
        if my_tree.get_left() != None:
            left_logic = no_odds(my_tree.get_left()) 
        if my_tree.get_right() != None:
            right_logic = no_odds(my_tree.get_right())
        return left_logic and right_logic

# Converts a binary tree into a  nested list in preorder
def convert_tree_to_list(b_tree):
    if b_tree== None:
        return None
    else:
        nested_list = []
        nested_list += [b_tree.get_data(), convert_tree_to_list(b_tree.get_left()), convert_tree_to_list(b_tree.get_right())]
        return nested_list

# Takes a binary tree and searches for the item parameter
# Returns true if the item is found
def search(tree, item):
    if tree == None:
        return False
    else:
        if tree.get_data() == item:
            return True
        else:
            return search(tree.get_left(), item) or search(tree.get_right(), item)
