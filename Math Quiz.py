'''
Mathematical Quiz

Author: Electra Bree
UPI: rbre269
AUID: 574069100
'''

import random

def display_intro():
    stars = "*" * 24
    print(stars)
    print("** A Simple Math Quiz **")
    print(stars)

def display_menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Integer Division")
    print("5. Exit")

def display_separator():
    dashes = "-" * 24
    print(dashes)

def get_user_input():
    number = int(input("Enter your choice: "))
    if number > 5:
        while number > 5:
            print("Invalid menu option.")
            number = int(input("Please try again: "))
    return number

def get_user_solution(problem):
    answer = int(input(problem))
    return answer

def check_solution(user_solution, solution, count):
    if user_solution == solution:
        print("Correct.")
        count = count + 1
    else:
        print("Incorrect.")
    return count

def menu_option(index, count):
    number1 = random.randrange(1,21)
    number2 = random.randrange(1,21)
    correct_solution = ""
    if index == 1:
        operation = "+"
        correct_solution = number1 + number2
    elif index == 2:
        operation = "-"
        correct_solution = number1 - number2
    elif index == 3:
        operation = "*"
        correct_solution = number1 * number2
    elif index == 4:
        operation = "//"
        correct_solution = number1 // number2
    problem = str(number1) + " " + operation + " " + str(number2) + " = "
    user_solution = get_user_solution(problem)
    correct_count = check_solution(user_solution, correct_solution, count)
    return correct_count

def display_result(total, correct):
    score = round(correct / total * 100, 2)
    print("You answered " + str(total) + " questions with " \
         + str(correct) + " correct.")
    print("Your score is " + str(score) + "%. Thank you.")   
   
def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()
    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()
