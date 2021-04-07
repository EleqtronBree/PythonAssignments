"""
Lecture 7 Exercise - Functions

Author: Electra Bree
"""

# Question 1
# Define the sum_bigger_two() function which is passed three whole
# numbers. The function returns the total of the two bigger numbers.

def sum_bigger_two(number1, number2, number3):
    smallest_number = min(number1, number2, number3)
    total = number1 + number2 + number3
    bigger_two_sum = total - smallest_number
    return bigger_two_sum

print("1.", sum_bigger_two(1, 2, 3))
print("2.", sum_bigger_two(11, 12, 3))
print("3.", sum_bigger_two(6, 2, 5))

# Question 2
# Define the shorter_length() function which is passed two strings.
# The function returns the length of the shorter of the two strings.

def shorter_length(string1, string2):
    number1 = len(string1)
    number2 = len(string2)
    shorter_string = min(number1, number2)
    return shorter_string

print("1.", shorter_length("Flibbertigibbet", "Rigmarole"))
print("2.", shorter_length("Mollycoddle", "Cat"))
print("3.", shorter_length("Skullduggery", "Canoodle"))

# Question 3
# Define the last_and_first() function which is passed one string. The
# function returns a string made up of the last character followed by
# the first character (both in uppercase characters).


def last_and_first(string):
    last_letter = string[-1].upper()
    first_letter = string[0].upper()
    letters = last_letter + "" + first_letter
    return letters

print("1.", last_and_first("Crudivore"))
print("2.", last_and_first("Ornery"))
print("3.", last_and_first("Brouhaha"))

# Question 4
# Define the required_boxes() function which is passed a total number
# of items and the maximum number of items which fit into one box.
# The function returns the total number of boxes required (any
# leftovers always require an extra box).

import math

def required_boxes(maximum, total):
    total_boxes = math.ceil(maximum / total)
    return total_boxes

boxes_needed1 = required_boxes(30, 16)
boxes_needed2 = required_boxes(30, 3)
boxes_needed3 = required_boxes(30, 10)

print("1.", "Boxes:", boxes_needed1)
print("2.", "Boxes:", boxes_needed2)
print("3.", "Boxes:", boxes_needed3)

# Question 5
# Complete the two functions in the following program. The following
# program gets a first name from the user (prompt is "Enter name: ")
# and then removes a random letter from the name. The resulting
# name is printed. 

import random

def get_first_name():
    name = input("Enter name: ")
    return name
    
def remove_random_letter(name):
    random_letter = random.randrange(0, len(name))
    new_name = name[0:random_letter - 1] + "" + name[random_letter + 1:]
    return new_name
    
first_name = get_first_name()

version1 = remove_random_letter(first_name)
version2 = remove_random_letter(first_name)
version3 = remove_random_letter(first_name)

print("1.", version1)
print("2.", version2)
print("3.", version3)
    
