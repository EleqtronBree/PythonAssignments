"""
Author: Electra Bree

Calculates the memory score
"""

def get_memory_score(number_list):
    memory_list = []
    score = 0
    for number in number_list:
        if number not in memory_list:
            if len(memory_list) >= 5:
                memory_list.pop(0)
            memory_list.append(number)
        else:
            score += 1
    return score

print("1. ", get_memory_score([3, 4, 1, 6, 3, 3, 9, 0, 0, 0]))
print("2. ", get_memory_score([1, 2, 2, 2, 2, 3, 1, 1, 8, 2]))
print("3. ", get_memory_score([2, 2, 2, 2, 2, 2, 2, 2, 2]))
print("4. ", get_memory_score([1, 2, 3, 4, 5, 6, 7, 8, 9]))
random_nums5 = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
print("5. ", get_memory_score(random_nums5))
            
    
