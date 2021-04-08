"""
Random Password Generation

Author: Electra Bree
Username: rbre269
User ID: 574069100
"""

import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter1 = alphabet[random.randrange(0, 52)]
letter2 = alphabet[random.randrange(0, 52)]
letter3 = alphabet[random.randrange(0, 52)]
letter4 = alphabet[random.randrange(0, 52)]
random_number = "000" + str(random.randrange(0, 999))
four_digit_number = random_number[-4:]
lots_of_stars = "*" * 20

print(lots_of_stars)
print("*Password Generator*")
print(lots_of_stars)
print()
print("Your password is ", letter1, letter2, letter3, letter4, four_digit_number, sep = "")
