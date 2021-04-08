"""
Author: Electra Bree
Assignment related to recursion
"""

# Question 1
# Takes an integer and counts up to that integer
def count_up(n):
    if n == 0:
        print("Go!")
    else:
        count_up(n-1)
        print(n)

#Question 2
# Takes an integer and counts down from that integer
def count_up(n):
    if n == 0:
        print("Go!")
    else:
        count_up(n-1)
        print(n)

# Question 3
# Returns the number of uppercase letter in the parameter string
def count_upper(word):
    upper_cases = 0
    if word == "":
        return upper_cases
    else:
        if word[0].isupper():
            upper_cases = 1
        return upper_cases + count_upper(word[1:])

# Question 4
# Takes a list of integers and returns the number of odd integers in the given list
def count_odd_list(numbers):
    odd_integers = 0
    if numbers == []:
        return odd_integers
    else:
        if numbers[0] % 2 != 0:
            odd_integers += 1
        return odd_integers + count_odd_list(numbers[1:])

# Question 5
# takes an integer as a parameter and returns the value of the following series:
# m2(i) = 1/3 + 2/5 + 3/7 + 4/9 + i / ( 2 * i + 1)
def evaluate_m2(i):
    if i == 0:
        return 0
    else:
        return i / (2 * i + 1) + evaluate_m2(i - 1)

# Question 6
# Calculates and returns the sum of all odd integers in the list
def get_sum_odd_list(numbers):
    if numbers == []:
        return 0
    else:
        if numbers[0] % 2 == 1:
            return numbers[0] + get_sum_odd_list(numbers[1:])
        else:
            return get_sum_odd_list(numbers[1:])

# Question 7
# Calculates and returns the sum of all multiples of m in the list
def get_sum_multiple_list(numbers, m):
    if numbers == []:
        return 0
    else:
        if numbers[0] % m == 0:
            return numbers[0] + get_sum_multiple_list(numbers[1:], m)
        return get_sum_multiple_list(numbers[1:], m)

# Question 8
# Takes a list of integers as a parameter and returns a list of even numbers in the given parameter
def get_even_list(numbers):
    if numbers == []:
        return []
    else:
        if numbers[0] % 2 == 0:
            return [numbers[0]] + get_even_list(numbers[1:])
        return get_even_list(numbers[1:])

# Question 9
# Takes a list of integers as a parameter and returns False if the parameter list contains any odd values and returns True otherwise
def no_odds(numbers):
    if numbers == []:
        return True
    else:
        if numbers[0] % 2 == 1:
            return False
        return True and no_odds(numbers[1:])

# Question 10
# Performs a recursive binary search on a sorted list of numbers
def binary_search(values, item):
    first = 0
    last = len(values) - 1
    if first > last:
        return False
    else:
        mid = last -(first + last) // 2
        print(values[:mid], values[mid], values[mid+1:])
        if item == values[mid]:
            return True
        elif item < values[mid]:
            return binary_search(values[:mid], item)
        else:
            return binary_search(values[mid+1:], item)
