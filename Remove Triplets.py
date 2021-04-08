"""
Author: Electra Bree

Removes triplet numbers from a list
"""

def remove_triplets(number_list):
    index = 0
    repeat = 1
    old_number = '' 

    for number in number_list:
        if old_number == '':
            old_number = number
        elif old_number == number:
            repeat += 1
        else:
            repeat = 1
        if repeat == 3:
            number_list[index] = 0
            number_list[index - 1] = 0
            number_list[index - 2] = 0
            repeat = 0
        old_number = number
        index +=1
        
    while 0 in number_list:
        number_list.pop(number_list.index(0))
        

a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3]
remove_triplets(a_list)
print("1.", a_list)
a_list = [6, 6, 6, 7, 6, 6, 6, 6, 6]
remove_triplets(a_list)
print("2.", a_list)
a_list = [6, 6, 6, 7, 6, 6, 4, 3, 3, 3, 8, 8, 8, 3]
remove_triplets(a_list)
print("3.", a_list)
a_list = [1, 1, 1, 4, 4, 4, 1, 1, 1]
remove_triplets(a_list)
print("4.", a_list)
a_list = [1, 1, 2, 1, 2, 2]
remove_triplets(a_list)
print("5.", a_list)
