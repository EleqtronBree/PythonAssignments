"""
Author: Electra Bree

Checks if a given code is valid
"""

def is_a_valid_code(string):
    code_letters = ["S", "B", "N", "T", "P"]
    min_for_each_letter = [1, 3, 4, 0, 3] #inclusive
    max_for_each_letter = [7, 9, 6, 7, 5] #inclusive
    code_list = list(string)
    word = ''
    number = ''
    min_number = 0
    max_number = 0
    
    for element in code_list:
        if element.isdigit():
            if int(element) < min_number or int(element) > max_number:
                number = False
            if number == '':
                number = True
        else:
            if element in code_letters:
                if word == '':
                    word = True
                    position = code_letters.index(element)
                    min_number = min_for_each_letter[position]
                    max_number = max_for_each_letter[position]
                else:
                    word = False
    if number == '':
        number = False
                
    if word and number:
        return True
    else:
        return False


print("1.", is_a_valid_code('B747346'))
print("2.", is_a_valid_code('N  444  454'))
print("3.", is_a_valid_code('T 400 4854'))
print("4.", is_a_valid_code('S  444S454'))
print("5.", is_a_valid_code('P  '))
print("6.", is_a_valid_code('T  0  '))
