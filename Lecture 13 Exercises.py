'''
Lecture 13 Exercise

Author: Electra Bree
'''

# Question 1
'''
Complete the for…in loop.
'''

for number in range(7, 24, 3):
    print(number, end = " ")
print()

for value in range(30, -15, -5):
    print(value, end = " ")
print()

# Question 2
'''
An amount doubles each year. Using a for…in loop
complete the double_each_year() function
which prints the growth of the parameter value,
(start_amt) for the given number of years
(num_years). The first line printed by the function
is the starting amount.
Each line of the output is numbered starting from the
number 1. The function returns the final amount.
'''

def double_each_year(start_amt, num_years):
    print("Starting with: ", start_amt)
    for number in range(1, num_years + 1):
        start_amt *= 2
        print(str(number) + ": ", start_amt)
    return start_amt
        

def main():
    print("After 4 years:",double_each_year(24, 4))
    print("After 3 years:", double_each_year(235, 3))
    print("After 5 years:", double_each_year(15, 5))

main()

# Question 3
'''
Using a for…in loop complete the print_series() function
which prints a series of numbers starting from the parameter value,
start_num. The second number printed is the first number plus
1, the third number is the second number plus 2, the fourth number
is the third number plus 3, and so on
'''

def print_series(start_num, how_many):
    factor = 0
    for number in range(start_num, how_many + 1):
        print(number, end = " ")
        factor = factor + 1
        
def main():
    print_series(2, 8)
    print_series(5, 12)
    print_series(16, 9)

main()

# Question 4
'''
Convert the following while loop into a for…in range(…) loop:
'''

for counter in range(12, 260, 10):
    print(counter)

num = 45

while num > 3:
    print(num * 2)
    num = num - 5

# Question 5
'''
The get_series_sum() function returns the sum of the given
number of terms of the series:
e.g., get_series_sum(4) returns the sum of one half plus one
quarter plus one eighth plus one sixteenth. Complete the function
'''

def get_series_sum(num_terms):
    total = 1/2
    for sequence in range(2, num_terms, 2):
        total = total + 1/(sequence + 2)
    return total

def main():
    for num in range(1, 10):
        comment = "Terms: " + str(num) + " Sum:"
        print(comment, get_series_sum(num))
main()
