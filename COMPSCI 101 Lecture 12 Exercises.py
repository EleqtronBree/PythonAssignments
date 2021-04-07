"""
Lecture 12 Exercise

Author: Electra Bree
"""

# Question 2
'''
For an integer, a divisor is a number which divides exactly into the
integer (a factor of the integer), e.g., the divisors of 6 are 1, 2, 3, 6.
Complete the get_all_divisors() function. Note that 1 and the
number itself are divisors (as they divide into the number exactly).
'''

def get_divisor_string(number):
	divisor = 1
	div_string = ""
	while divisor <= number // 2:
		if number % divisor == 0:
			div_string += str(divisor) + " "
		divisor += 1
		
	div_string += str(number) 
	return div_string     

def main():
    print(get_divisor_string(24))
    print(get_divisor_string(25))
    print(get_divisor_string(5628))

main()

# Question 3
'''
The get_dice_throws_result() function throws a number of dice
(given by num_dice_throws) and counts how often the dice value,
dice_to_check occurs. Complete the function.
'''
import random

def get_dice_throws_result(num_dice_throws, dice_to_check):
    sixes = 0
    while num_dice_throws > 0:
        throws = random.randrange(1,7)
        num_dice_throws -= 1
        if throws == dice_to_check:
            sixes += 1
    return sixes

def main():
    print(get_dice_throws_result(30000, 6), "sixes thrown (out of 30000 throws)")
    print(get_dice_throws_result(6, 6), "sixes thrown (out of 6 throws)")
    print(get_dice_throws_result(600000, 6), "sixes thrown (out of 600000 throws)")

main()

# Question 4
'''
A perfect number is an integer that is equal to the sum of its
divisors (excluding the number itself), e.g., 28 = 1 + 2 + 4 + 7 + 14.
Complete the following two functions. The check_perfection()
function checks for perfection and prints either' # is a perfect
number'or'# is NOT a perfect number'.
'''

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

def main():
    check_perfection(28)
    check_perfection(54)
    check_perfection(496)

main()

# Question 5
'''
The get_legal_number() function repeatedly prompts the user for a
number until the user number is within (both inclusive) the two
numbers passed as parameters. The function returns the user
number. Complete the function:
'''

def get_legal_user_num(lower, upper):
    prompt = "Enter a number ("
    prompt = prompt + str(lower) + "-" + str(upper) + "): "
    number = int(input(prompt))
    while number < lower or number > upper:
        number = int(input(prompt))
    return number

def main():
    print(get_legal_user_num(0, 6))
    print(get_legal_user_num(10, 20))
    print(get_legal_user_num(1, 2))
main()

# Question 6
'''
The following function keeps prompting the user to guess a hidden
number until the user correctly guesses the number. At each guess
the function lets the user know if the guess is too high or too low.
The function also keeps track of (and prints) the number of guesses.
Complete the user_number_guess() function:
'''

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

def main():
    user_number_guess(random.randrange(1, 100))
main()
