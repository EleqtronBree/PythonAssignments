"""
Lecture 10 Exercise

Author: Electra Bree
"""

# Question 3
'''
Complete the print_message() function which has an equal chance
of printing "now", "soon" and "never". 
'''

import random

def print_message():
    number = random.randrange(0,30)
    if number <= 10:
        print("now")
    if number > 10 and number <= 20:
        print("soon")
    if number > 20:
        print("never")
    
def main():
    print("Life will improve")
    print_message()
    
main()

# Question 6
'''
Complete the get_price() function which returns the cost of tickets.
If the number of tickets is 14 or more, a 10% discount applies.
'''

def get_price(child, adult):
    child_price = 10
    adult_price = 25
    group_size = 14
    group_rate = 0.9
    cost = (child * child_price + adult * adult_price)
    if group_size >= 14:
        cost = cost * group_rate
    return cost

def main():
    num_child = int(input("Enter the number of children: "))
    num_adult = int(input("Enter the number of adults: "))
    cost = get_price(num_child, num_adult)
    print("The cost of your tickets is: $" + str(cost))

main()

# Question 7
'''
Many countries have 50 years as their standard length of copyrights
and when a work's copyright term ends, the work passes into the
public domain. Complete the function below which which prints
"Out of copyright" if the author has been dead 50 years or more.
'''

def copyright_check(current_year, death_year):
    years_difference = current_year - death_year
    if death_year >= 50:
        print("Out of copyright")
    
def main():
    current_year = 2016
    author_death_year = input("Enter year of author's death: ")
    author_death_year = int(author_death_year)
    copyright_check(current_year, author_death_year)

main()
