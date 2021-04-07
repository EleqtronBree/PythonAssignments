"""
Lecture 8 Exercise - More Functions

Author: Electra Bree
"""

# Question 1
'''
Complete the get_discount() function which returns the discount
amount (a float number rounded to 2 decimal places). The function
is passed two arguments, the amount and the discount rate.
'''

def get_discount(amount, rate):
    discount_amount = round(amount * rate / 100, 2)
    return discount_amount

discount_message = "Discount: $" + str(get_discount(234, 5))
print(discount_message)
discount_message = "Discount: $" + str(get_discount(125, 15))
print(discount_message)

# Question 2
'''
Complete the get_discount_message() function which returns a string
made up of the rate of discount, followed by the string "% Discount:
$", followed by the discount amount. The function has two
parameters, the discount amount and the discount rate.
'''

def get_discount_message(discount, rate):
    message = str(rate) + "% Discount: $" + str(discount)
    return message
    
message = get_discount_message(11.7, 5)
print(message)
message = get_discount_message(98.55, 15)
print(message)

# Question 3
'''
Complete the print_docket() function which prints the sales docket
information (the format should be as shown in the output shown).
The function is passed two arguments, the cost price and the
discount rate. Your function code MUST make a call to both the
functions: get_discount(), get_discount_message().
'''

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

# Question 4
'''
The following program prompts the user for a number of items to be
packaged. Each box can hold 10 items. Any left over items require
an extra box. The first 6 boxes cost $8 each and any boxes above the
first 6, cost $5 each. The program executes as shown in the example
outputs below. Design the functions needed to write this program
and write the main code for the program.
'''

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

def main(items_per_box ):
    items = get_items()
    boxes = boxes_needed(items_per_box , items)
    cost = calculate_cost(boxes)
    
    print()
    print("Items: " + str(items))
    print("Boxes needed: " + str(boxes))
    print("Cost: $" + str(cost))

items_per_box = 10
print()
main(items_per_box)
print()

# Question 5
'''
The following program has two errors. What are the errors? Write a
correction for each error.
The desired output is shown below the program.
'''

def display_winner_details(winner, score):
    message = "*** " + winner.upper() + " (" + str(score) + ") ***"
    print(message)
    
score = 50
display_winner_details("Jo Li", score)
print(score)


