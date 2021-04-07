"""
Author: Electra Bree

Gets the most recent number in two given lists
"""

def get_most_recent(number_list, test_list):
    recent_number = -1
    for number in number_list:
        if number in test_list:
            recent_number = number
    return recent_number

print("1.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [2, 0, 3]))
print("2.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [0, 7, 2]))
print("3.", get_most_recent([0, 1, 2, 8, 9, 0, 3, 4, 6], [1, 9, 2, 8]))
print("4.", get_most_recent([4, 1, 4, 5, 4, 1], [0, 7, 3]))
print("5.", get_most_recent([8, 1, 2, 0, 8, 4, 1], [8, 7, 3]))
print("6.", get_most_recent([], [8, 1, 0, 3]))
numbers = [1, 1, 1, 0, 1, 0, 2, 2, 1, 2, 0, 1, 2, 0, 3, 4, 1, 2, 4, 0, 3, 8, 8, 5, 5]
print("7.", get_most_recent(numbers, [1, 0, 3, 4] ))
numbers = [1, 2, 2, 2, 2, 3, 1, 3, 8, 0]
print("8.", get_most_recent(numbers, [1, 8, 2, 3, 4, 2]))
