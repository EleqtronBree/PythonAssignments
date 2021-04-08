"""
Author: Electra Bree
Assignment related to sorting
"""

import math 

# Question 1
# Takes a list of numbers and an index integer, swaps each pair of adjacent elements if they're not in order until the index position.
# Assumes the list is not empty
def bubble_row(data, index):
    for j in range(index):
        if data[j] > data[j + 1]:
            first_number = data[j]
            second_number = data[j + 1]
            data[j] = second_number
            data[j + 1] = first_number

# Question 2
# Takes a list of numbers and sorts the list using bubble sort algorithm.
def my_bubble_sort(a_list): 
    for pass_num in range(len(a_list)-1, 0, -1):
        for j in range(pass_num):
            if a_list[j] > a_list[j + 1]:
                first_number = a_list[j]
                second_number = a_list[j + 1]
                a_list[j] = second_number
                a_list[j + 1] = first_number

# Question 3
# Takes a list of numbers and an index integer, and returns the position of the largest element.
# Assumes the list is not empty
def get_largest_position(data, index):
    largest = data[0]
    for j in range(index + 1):
        if data[j] > largest:
            largest = data[j]
    return data.index(largest)

# Question 4
# Takes a list of numbers and index intenger.
# Selects the larget element and is swapped with the element at the index position. Assumes the list is not empty
def selection_row(data, index):
    position_largest = get_largest_position(data, index)
    if data[position_largest] > data[index]:
        first_number = data[position_largest]
        second_number = data[index]
        data[position_largest] = second_number
        data[index] = first_number

# Question 5
# Takes a list of numbers and sorts the list using Selection sort algorithm
def my_selection_sort(data):	
    for pass_num in range(len(data) - 1, 0, -1):
        index_largest = 0
        for j in range(pass_num + 1): #iterate through data
            if data[j] >= data[index_largest]:
                index_largest = j
        #got largest index
        #switch numbers
        first_number = data[index_largest] #larger number
        second_number = data[pass_num] #smaller number
        data[index_largest] = second_number
        data[pass_num] = first_number

# Question 6
# Takes a list of numbers and index integer, and checks for the correct placement for the element starting from the index position.
# Shifts all elements one place to the right until a suitable position is found for the new element
def shifting(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and (data[i] > item_to_check):
        data[i+1] = data[i]
        i -= 1

# Question 7
# Takes a list of numbers and index integer
# Checks for correct placement of the element from the index position and shifts all elements one place to the right until the correct position is found and replaces it
def insertion_row(data, index):	
    item_to_insert = data[index]
    i = index - 1
    while  i>= 0 and data[i] > item_to_insert:
        data[i+1] = data[i]
        i -= 1
    data[i + 1] = item_to_insert

# Question 8
# Implementation of the Insertion sort algorithm
def my_insertion_sort(a_list):	
    for index in range(1, len(a_list)):
	item_to_insert = a_list[index]
	i = index - 1
	while i >= 0 and a_list[i] > item_to_insert:
	    a_list[i + 1] = a_list[i]
	    i -= 1
	a_list[i + 1] = item_to_insert

# Question 9
# Implementation of the Binary search algorithm
def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_index = math.ceil((min_index + max_index)/2)
        if numbers[mid_index] == value:
            return mid_index
        elif numbers[mid_index] < value:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return -1        
