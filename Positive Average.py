"""
Author: Electra Bree

Gets the average of a list if there are no negative numbers present
"""

def get_funny_average(number_list):
    average = 0.0
    if len(number_list) > 0:
        while min(number_list) < 1:
            number_list.pop(number_list.index(min(number_list)))
        for number in range(1,3,1):
            number_list.pop(number_list.index(min(number_list)))
        if len(number_list) > 0:
            average = round(sum(number_list) / len(number_list), 1)
    return average

print("1.  [ 3, 2, 0, 25, 1]:                ", get_funny_average([ 3, 2, 0, 25, 1]))
print("2.  [-6, -32, 2, 0, -51, 1, 0, 0]:    ", get_funny_average([-6, -32, 2, 0, -51, 1, 0, 0]))
print("3.  [56, 32, 2, 22, 22]:              ", get_funny_average([56, 32, 2, 22, 22]))
print("4.  [-56, -3, 0, -21, 0, 6, 5]:       ", get_funny_average([-56, -3, 0, -21, 0, 6, 5]))
print("5.  [56, 3, 2, 0, 251, 1, 41, 22]:    ", get_funny_average([56, 3, 2, 0, 251, 1, 41, 22]))
print("6.  [-56, -3, 2, 0, -251, 1, -41, 0]: ", get_funny_average([-56, -3, 2, 0, -251, 1, -41, 0]))
print("7.  []:                               ", get_funny_average([]))
    
