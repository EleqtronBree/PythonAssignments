  
"""
Author: Electra Bree
Exercises from the COMPSCI 101 course
"""

import random
import math

# Question 1
"""
Complete the print_message() function which has an equal chance
of printing "now", "soon" and "never". 
"""

import random

def print_message():
    number = random.randrange(0,30)
    if number <= 10:
        print("now")
    if number > 10 and number <= 20:
        print("soon")
    if number > 20:
        print("never")
    
print("Life will improve")
print_message()

# Question 2
"""
Complete the get_price() function which returns the cost of tickets.
If the number of tickets is 14 or more, a 10% discount applies.
"""

def get_price(child, adult):
    child_price = 10
    adult_price = 25
    group_size = 14
    group_rate = 0.9
    cost = (child * child_price + adult * adult_price)
    if group_size >= 14:
        cost = cost * group_rate
    return cost

num_child = int(input("Enter the number of children: "))
num_adult = int(input("Enter the number of adults: "))
cost = get_price(num_child, num_adult)
print("The cost of your tickets is: $" + str(cost))

# Question 3
"""
Many countries have 50 years as their standard length of copyrights
and when a work's copyright term ends, the work passes into the
public domain. Complete the function below which which prints
"Out of copyright" if the author has been dead 50 years or more.
"""

def copyright_check(current_year, death_year):
    years_difference = current_year - death_year
    if death_year >= 50:
        print("Out of copyright")
    
current_year = 2016
author_death_year = input("Enter year of author's death: ")
author_death_year = int(author_death_year)
copyright_check(current_year, author_death_year)

# Question 4
"""
Complete the add_bonus() function which prints "Good job!" and
returns 30000 plus the salary if the parameter is a value greater
than 150000. Otherwise it prints "Excellent performance!" and
returns 300 plus the salary.
"""

def add_bonus(salary):
    if salary > 150000:
        print("Good job!")
        salary = salary + 30000
    else:
        print("Excellent performance!")
        salary = salary + 300
    return salary
        

salary = 34000
new_salary = add_bonus(salary)
print("old salary: $" + str(salary))
print("new salary: $" + str(new_salary))
print()
salary = 250000
new_salary = add_bonus(salary)
print("old salary: $" + str(salary))
print("new salary: $" + str(new_salary))

# Question 5
"""
Complete the compare_nums1() function which is passed two
integers and returns a string. The function compares the first
number to the second number and returns one of the following
three strings (i.e., the string which is applicable):
"equal to" OR
"less than" OR
"greater than"
"""

def compare_nums1(num1, num2):
    if num1 > num2:
        comparison = "greater than"
    if num1 == num2:
        comparison = "equal to"
    if num1 < num2:
        comparison = "less than"
    return comparison

num1 = random.randrange(1, 100)
num2 = random.randrange(1, 100)
comparison = compare_nums1(num1, num2)
print(num1, "is", comparison, num2)

# Question 6
"""
Complete the compare_nums2() function which is passed two
integers and returns a string. The function compares the first
number to the second number and returns one of the following
three strings (i.e., the string which is applicable):
"equal to" OR
"less than" OR
"greater than"
"""

import random

def compare_nums2(num1, num2):
    if num1 > num2:
        comparison = "greater than"
    elif num1 == num2:
        comparison = "equal to"
    elif num1 < num2:
        comparison = "less than"
    return comparison

num1 = random.randrange(1, 100)
num2 = random.randrange(1, 100)
comparison = compare_nums2(num1, num2)
print(num1, "is", comparison, num2)

# Question 7
"""
A year is a leap year if it is divisible by 400, or 'divisible by 4 but not
divisible by 100', e.g., 1900, 2011 and 2100 are not a leap years
whereas 2000, 2008 and 2400 are leap years. Complete the
is_leap_year() function:
"""

def is_leap_year(year):
    if year / 400 == int(year / 400):
        return "True"
    elif year / 4 == int(year / 4) and not year / 100 == int(year / 100):
        return "True"
    else:
        return "False"  

print(is_leap_year(1900))
print(is_leap_year(2011))
print(is_leap_year(2100))
print(is_leap_year(2000))
print(is_leap_year(2008))
print(is_leap_year(2400))

# Question 8
"""
For an integer, a divisor is a number which divides exactly into the
integer (a factor of the integer), e.g., the divisors of 6 are 1, 2, 3, 6.
Complete the get_all_divisors() function. Note that 1 and the
number itself are divisors (as they divide into the number exactly).
"""

def get_divisor_string(number):
	divisor = 1
	div_string = ""
	while divisor <= number // 2:
		if number % divisor == 0:
			div_string += str(divisor) + " "
		divisor += 1
		
	div_string += str(number) 
	return div_string     

print(get_divisor_string(24))
print(get_divisor_string(25))
print(get_divisor_string(5628))

# Question 9
"""
The get_dice_throws_result() function throws a number of dice
(given by num_dice_throws) and counts how often the dice value,
dice_to_check occurs. Complete the function.
"""

def get_dice_throws_result(num_dice_throws, dice_to_check):
    sixes = 0
    while num_dice_throws > 0:
        throws = random.randrange(1,7)
        num_dice_throws -= 1
        if throws == dice_to_check:
            sixes += 1
    return sixes

print(get_dice_throws_result(30000, 6), "sixes thrown (out of 30000 throws)")
print(get_dice_throws_result(6, 6), "sixes thrown (out of 6 throws)")
print(get_dice_throws_result(600000, 6), "sixes thrown (out of 600000 throws)")

# Question 10
"""
A perfect number is an integer that is equal to the sum of its
divisors (excluding the number itself), e.g., 28 = 1 + 2 + 4 + 7 + 14.
Complete the following two functions. The check_perfection()
function checks for perfection and prints either' # is a perfect
number'or'# is NOT a perfect number'.
"""

def get_divisor_sum(number):
    divisor = 1
    total_number = 0
    while divisor <= number // 2:
        if number % divisor == 0:
            total_number += divisor
        divisor += 1
    return total_number

def check_perfection(number):
    divisor = get_divisor_sum(number)
    if number == divisor:
        print(str(number) + " is a perfect number")
    else:
        print(str(number) + " is NOT a perfect number")

check_perfection(28)
check_perfection(54)
check_perfection(496)

# Question 11
"""
The get_legal_number() function repeatedly prompts the user for a
number until the user number is within (both inclusive) the two
numbers passed as parameters. The function returns the user
number. Complete the function:
"""

def get_legal_user_num(lower, upper):
    prompt = "Enter a number ("
    prompt = prompt + str(lower) + "-" + str(upper) + "): "
    number = int(input(prompt))
    while number < lower or number > upper:
        number = int(input(prompt))
    return number

print(get_legal_user_num(0, 6))
print(get_legal_user_num(10, 20))
print(get_legal_user_num(1, 2))

# Question 12
"""
The following function keeps prompting the user to guess a hidden
number until the user correctly guesses the number. At each guess
the function lets the user know if the guess is too high or too low.
The function also keeps track of (and prints) the number of guesses.
Complete the user_number_guess() function:
"""

def user_number_guess(computer_num):
    prompt = "Enter your guess (1 - 99): "
    guess = 0
    guesses = 0
    while guess != computer_num:
        guess = int(input(prompt))
        guesses += 1
        if guess < computer_num:
            print("Too low")
        elif guess > computer_num:
            print("Too high")
        else:
            print("Correct! Number of guesses: " + str(guesses))

user_number_guess(random.randrange(1, 100))

# Question 13
"""
Complete the for…in loop.
"""

for number in range(7, 24, 3):
    print(number, end = " ")
print()

for value in range(30, -15, -5):
    print(value, end = " ")
print()

# Question 14
"""
An amount doubles each year. Using a for…in loop
complete the double_each_year() function
which prints the growth of the parameter value,
(start_amt) for the given number of years
(num_years). The first line printed by the function
is the starting amount.
Each line of the output is numbered starting from the
number 1. The function returns the final amount.
"""

def double_each_year(start_amt, num_years):
    print("Starting with: ", start_amt)
    for number in range(1, num_years + 1):
        start_amt *= 2
        print(str(number) + ": ", start_amt)
    return start_amt
        
print("After 4 years:",double_each_year(24, 4))
print("After 3 years:", double_each_year(235, 3))
print("After 5 years:", double_each_year(15, 5))

# Question 15
"""
Using a for…in loop complete the print_series() function
which prints a series of numbers starting from the parameter value,
start_num. The second number printed is the first number plus
1, the third number is the second number plus 2, the fourth number
is the third number plus 3, and so on
"""

def print_series(start_num, how_many):
    factor = 0
    for number in range(start_num, how_many + 1):
        print(number, end = " ")
        factor = factor + 1
        
print_series(2, 8)
print_series(5, 12)
print_series(16, 9)

# Question 16
"""
Convert the following while loop into a for…in range(…) loop:
"""

for counter in range(12, 260, 10):
    print(counter)

num = 45

while num > 3:
    print(num * 2)
    num = num - 5

# Question 17
"""
The get_series_sum() function returns the sum of the given
number of terms of the series:
e.g., get_series_sum(4) returns the sum of one half plus one
quarter plus one eighth plus one sixteenth. Complete the function
"""

def get_series_sum(num_terms):
    total = 1/2
    for sequence in range(2, num_terms, 2):
        total = total + 1/(sequence + 2)
    return total

for num in range(1, 10):
    comment = "Terms: " + str(num) + " Sum:"
    print(comment, get_series_sum(num))

# Question 18
"""
Define the sum_bigger_two() function which is passed three whole
numbers. The function returns the total of the two bigger numbers.
"""

def sum_bigger_two(number1, number2, number3):
    smallest_number = min(number1, number2, number3)
    total = number1 + number2 + number3
    bigger_two_sum = total - smallest_number
    return bigger_two_sum

print("1.", sum_bigger_two(1, 2, 3))
print("2.", sum_bigger_two(11, 12, 3))
print("3.", sum_bigger_two(6, 2, 5))

# Question 19
"""
Define the shorter_length() function which is passed two strings.
The function returns the length of the shorter of the two strings.
"""

def shorter_length(string1, string2):
    number1 = len(string1)
    number2 = len(string2)
    shorter_string = min(number1, number2)
    return shorter_string

print("1.", shorter_length("Flibbertigibbet", "Rigmarole"))
print("2.", shorter_length("Mollycoddle", "Cat"))
print("3.", shorter_length("Skullduggery", "Canoodle"))

# Question 20
"""
Define the last_and_first() function which is passed one string. The
function returns a string made up of the last character followed by
the first character (both in uppercase characters).
"""

def last_and_first(string):
    last_letter = string[-1].upper()
    first_letter = string[0].upper()
    letters = last_letter + "" + first_letter
    return letters

print("1.", last_and_first("Crudivore"))
print("2.", last_and_first("Ornery"))
print("3.", last_and_first("Brouhaha"))

# Question 21
"""
Define the required_boxes() function which is passed a total number
of items and the maximum number of items which fit into one box.
The function returns the total number of boxes required (any
leftovers always require an extra box).
"""

def required_boxes(maximum, total):
    total_boxes = math.ceil(maximum / total)
    return total_boxes

boxes_needed1 = required_boxes(30, 16)
boxes_needed2 = required_boxes(30, 3)
boxes_needed3 = required_boxes(30, 10)

print("1.", "Boxes:", boxes_needed1)
print("2.", "Boxes:", boxes_needed2)
print("3.", "Boxes:", boxes_needed3)

# Question 22
"""
Complete the two functions in the following program. The following
program gets a first name from the user (prompt is "Enter name: ")
and then removes a random letter from the name. The resulting
name is printed.
"""

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

# Question 23
"""
Complete the get_discount() function which returns the discount
amount (a float number rounded to 2 decimal places). The function
is passed two arguments, the amount and the discount rate.
"""

def get_discount(amount, rate):
    discount_amount = round(amount * rate / 100, 2)
    return discount_amount

discount_message = "Discount: $" + str(get_discount(234, 5))
print(discount_message)
discount_message = "Discount: $" + str(get_discount(125, 15))
print(discount_message)

# Question 24
"""
Complete the get_discount_message() function which returns a string
made up of the rate of discount, followed by the string "% Discount:
$", followed by the discount amount. The function has two
parameters, the discount amount and the discount rate.
"""

def get_discount_message(discount, rate):
    message = str(rate) + "% Discount: $" + str(discount)
    return message
    
message = get_discount_message(11.7, 5)
print(message)
message = get_discount_message(98.55, 15)
print(message)

# Question 25
"""
Complete the print_docket() function which prints the sales docket
information (the format should be as shown in the output shown).
The function is passed two arguments, the cost price and the
discount rate. Your function code MUST make a call to both the
functions: get_discount(), get_discount_message().
"""

def get_discount(amount, rate):
    discount_amount = round(amount * rate / 100, 2)
    return discount_amount
    
def get_discount_message(discount, rate):
    message = str(rate) + "% Discount: $" + str(discount)
    return message
    
def print_docket(cost, discount_rate):
    print("Original price $" + str(cost))
    discount_cost = get_discount(cost, discount_rate)
    new_cost = cost - discount_cost
    print(get_discount_message(discount_cost, discount_rate))
    print("Price $" + str(new_cost))
    
print_docket(234, 5)
print()
print_docket(657, 15)

# Question 26
"""
The following program prompts the user for a number of items to be
packaged. Each box can hold 10 items. Any left over items require
an extra box. The first 6 boxes cost $8 each and any boxes above the
first 6, cost $5 each. The program executes as shown in the example
outputs below. Design the functions needed to write this program
and write the main code for the program.
"""

import math

def get_items():
    items = int(input("Enter number of items: "))
    return items

def boxes_needed(maximum, items):
    boxes = math.ceil(items / maximum)
    return boxes

def calculate_cost(boxes):
    first_6 = min(boxes, 6)
    above_6 = boxes - 6
    above_6 = max(above_6, 0)
    cost = first_6 * 8 + above_6 * 5
    return cost

def box_main(items_per_box):
    items = get_items()
    boxes = boxes_needed(items_per_box , items)
    cost = calculate_cost(boxes)
    
    print()
    print("Items: " + str(items))
    print("Boxes needed: " + str(boxes))
    print("Cost: $" + str(cost))

items_per_box = 10
print()
box_main(items_per_box)
print()

# Question 27
"""
The following program has two errors. What are the errors? Write a
correction for each error.
The desired output is shown below the program.
"""

def display_winner_details(winner, score):
    message = "*** " + winner.upper() + " (" + str(score) + ") ***"
    print(message)
    
score = 50
display_winner_details("Jo Li", score)
print(score)
