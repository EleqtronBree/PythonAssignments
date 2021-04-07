"""
Lecture 11 Exercises

Author: Electra Bree
"""

# Question 2
'''
Complete the add_bonus() function which prints "Good job!" and
returns 30000 plus the salary if the parameter is a value greater
than 150000. Otherwise it prints "Excellent performance!" and
returns 300 plus the salary.
'''

def add_bonus(salary):
    if salary > 150000:
        print("Good job!")
        salary = salary + 30000
    else:
        print("Excellent performance!")
        salary = salary + 300
    return salary
        

def main():
    salary = 34000
    new_salary = add_bonus(salary)
    print("old salary: $" + str(salary))
    print("new salary: $" + str(new_salary))
    print()
    salary = 250000
    new_salary = add_bonus(salary)
    print("old salary: $" + str(salary))
    print("new salary: $" + str(new_salary))

main()

# Question 4
'''
Complete the compare_nums1() function which is passed two
integers and returns a string. The function compares the first
number to the second number and returns one of the following
three strings (i.e., the string which is applicable):
"equal to" OR
"less than" OR
"greater than"
'''

import random

def compare_nums1(num1, num2):
    if num1 > num2:
        comparison = "greater than"
    if num1 == num2:
        comparison = "equal to"
    if num1 < num2:
        comparison = "less than"
    return comparison

def main():
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    comparison = compare_nums1(num1, num2)
    print(num1, "is", comparison, num2)

main()

# Question 5
'''
Complete the compare_nums2() function which is passed two
integers and returns a string. The function compares the first
number to the second number and returns one of the following
three strings (i.e., the string which is applicable):
"equal to" OR
"less than" OR
"greater than"
'''

import random

def compare_nums2(num1, num2):
    if num1 > num2:
        comparison = "greater than"
    elif num1 == num2:
        comparison = "equal to"
    elif num1 < num2:
        comparison = "less than"
    return comparison

def main():
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    comparison = compare_nums2(num1, num2)
    print(num1, "is", comparison, num2)

main()

# Question 6
'''
A year is a leap year if it is divisible by 400, or 'divisible by 4 but not
divisible by 100', e.g., 1900, 2011 and 2100 are not a leap years
whereas 2000, 2008 and 2400 are leap years. Complete the
is_leap_year() function:
'''
def is_leap_year(year):
    if year / 400 == int(year / 400):
        return "True"
    elif year / 4 == int(year / 4) and not year / 100 == int(year / 100):
        return "True"
    else:
        return "False"  

def main():
    print(is_leap_year(1900))
    print(is_leap_year(2011))
    print(is_leap_year(2100))
    print(is_leap_year(2000))
    print(is_leap_year(2008))
    print(is_leap_year(2400))

main()
