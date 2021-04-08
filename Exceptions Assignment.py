"""
Author: Electra Bree
Assignment related to exceptions
"""

#Question 1
"""
Write a boolean-valued function is_old_enough(age) which returns True if the given age value is 16 or more.
Otherwise the function should return False. If the age value is invalid, the function should return ERROR: Invalid age! (i.e. age < 0 or is of the wrong type).
Note: You *must* use the 'try... except' syntax and 'raise' in your solution.
"""

def is_old_enough(age):
    try:
        if age >= 16:
            return True
        elif age < 0:
            raise ValueError()
        else:
            return False
    except:
        return("ERROR: Invalid age!")

#Question 2
"""
Write a boolean-valued function is_valid_score(score) which returns True if the given score value is between 0 to 100.
If the score value is invalid (i.e. score < 0 or score > 100 or is of the wrong type),
the function should return ERROR: Invalid score!
Note: You *must* use the 'try... except' syntax and 'raise' in your solution.
"""

def is_valid_score(score):
    try:
        if score >= 0 and score <= 100:
            return True
        elif score < 0 or score > 100:
            raise ValueError()
    except (ValueError, TypeError):
        return "ERROR: Invalid score!"

#Question 3
"""
Write a function count_vowels(word) which takes a string as a parameter and returns the number of vowels in the parameter string.
If the parameter string is invalid (i.e. of the wrong type), the function should return ERROR: Invalid input!.
"""

def count_vowels(word):
    try:
        count = 0
        vowels = "aeiouAEIOU"
        for letter in word:
            if type(letter) == str:
                if letter in vowels:
                    count += 1
            else:
                raise TypeError()
    except TypeError:
        return "ERROR: Invalid input!"
    else:
        return count

#Question 4
"""
Write a function named get_min(numbers) which takes a list of numbers (ints or floats) as a parameter and returns the minimum value (as a float) in the numbers list.
If the parameter list contains any invalid values (i.e invalid type), the function should return ERROR: Invalid number!
You can assume that the parameter list is not empty.
"""

def get_min(numbers):
    try:
        min_number = numbers[0]
        for number in numbers:
            if number == "NA":
                raise TypeError()
            else:
                if number < min_number:
                    min_number = float(number)
    except TypeError:
        return "ERROR: Invalid number!"
    else:
        return min_number

#Question 5
"""
Write a function named get_sum(numbers) which takes a list of values and returns the sum of the all the values in the list.
However, if the list contains any invalid values, the function should ignore them and continue to do the calculation. 
"""

def get_sum(numbers):
    count = 0
    for number in numbers:
        try:
            if number != "NA":
               count += number
            else:
                raise TypeError()
        except:
            count += 0
    return count

#Question 6
"""
Write a function named get_diff(numbers, index1, index2) which takes a list of values and two index positions as parameters and returns the difference of the two values at the specified index positions.
If the two index positions are within the range, calculate the difference.
Otherwise, the function should return an error message "ERROR: Out of range!".
"""

def get_diff(numbers, index1, index2):
    try:
        number = numbers[index1] - numbers[index2]
    except TypeError:
        return "ERROR: Invalid number!"
    except IndexError:
        return "ERROR: Out of range!"
    else:
        return number

#Question 7
"""
Write a function called get_french_word(dictionary, word) that takes such a dictionary and a word as parameters and returns the corresponding French word.
If the English word does not appear in the dictionary, then your function should return an error message to indicate that the particular word is not available
If the calculation could not be done, the function should return "ERROR: Invalid number!".
"""

def get_french_word(dictionary, word):
    try:
        if word in dictionary:
            return dictionary[word]
        else:
            raise KeyError()
    except:
        return("ERROR: " + word + " is not available.")

#Question 8
"""
Write a function called get_room(rooms_dictionary, course_number) that takes such a dictionary and a course number as parameters and returns the corresponding room number.
If the course number does not appear in the dictionary, then your function should return an error message to indicate that the particular course is not available.
If the course number is an empty string, the function should return an error message
"""

def get_room(rooms_dictionary, course_number):
    try:
        if course_number == "":
            raise NameError()
        elif course_number in rooms_dictionary:
            return rooms_dictionary[course_number]
        else:
            raise KeyError()
    except KeyError:
        return("ERROR: " + course_number + " is not available.")
    except NameError:
        return "ERROR: Invalid course number!"

#Question 9
"""
The function takes a filename as a parameter and returns the largest number in the file as a float.
Modify the above function and use a try-except-else block to handle exceptions that may occur and handle the FileNotFoundError in your solution.
Note: remember to close the file properly if the file can be opened. You can assume that the minimum number in the file is -9999.
If the file is empty the function returns -9999.
"""

def get_largest(filename):
    try:
        input_file = open(filename, 'r')
        lines = input_file.readlines()
        input_file.close()
        largest = -9999
        for line in lines:
            items_list = line.split()
            for element in items_list:
                try:
                    value = float(element)
                except:
                    value += 0
                finally:    
                    if value > largest:
                        largest = value
    except FileNotFoundError:
        return "ERROR: The file '"+ filename +"' does not exist."
    else:
        return largest
