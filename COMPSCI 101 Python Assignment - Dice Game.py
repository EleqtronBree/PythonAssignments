"""
Program of a Dice Game

Author: Electra Bree
Username: rbre269
User ID: 574069100
"""

import random

current_score = 0
top_star_banner = "*" * 45
bottom_star_banner = "*" * 29

print(top_star_banner)
print("REACH 100 IN THREE ROUNDS!  Initial total: ", current_score)
print(top_star_banner)

#First print()


dice_1 = str(random.randrange(1,7))
dice_2 = str(random.randrange(1,7))
dice_3 = str(random.randrange(1,7))
dice_4 = str(random.randrange(1,7))
dice_5 = str(random.randrange(1,7))

print("Round 1:")
print("Your dice:", dice_1, dice_2, dice_3, dice_4, dice_5)

first_dice = int(input("  Tens? "))
second_dice = int(input("  Units? "))
dice_value = first_dice * 10 + second_dice
current_score = dice_value + current_score

print("Dice value: ", dice_value)
print("Your current total: ", current_score)
print()

#Second Round
dice_1 = str(random.randrange(1,7))
dice_2 = str(random.randrange(1,7))
dice_3 = str(random.randrange(1,7))
dice_4 = str(random.randrange(1,7))
dice_5 = str(random.randrange(1,7))

print("Round 2:")
print("Your dice:", dice_1, dice_2, dice_3, dice_4, dice_5)

first_dice = int(input("  Tens? "))
second_dice = int(input("  Units? "))
dice_value = first_dice * 10 + second_dice
current_score = dice_value + current_score

print("Dice value: ", dice_value)
print("Your current total: ", current_score)
print()

#Third Round
dice_1 = str(random.randrange(1,7))
dice_2 = str(random.randrange(1,7))
dice_3 = str(random.randrange(1,7))
dice_4 = str(random.randrange(1,7))
dice_5 = str(random.randrange(1,7))

print("Round 3:")
print("Your dice:", dice_1, dice_2, dice_3, dice_4, dice_5)

first_dice = int(input("  Tens? "))
second_dice = int(input("  Units? "))
dice_value = first_dice * 10 + second_dice
current_score = dice_value + current_score

print("Dice value: ", dice_value)
print("Your current total: ", current_score)
print()

remainder = abs(100 - current_score)

print(bottom_star_banner)
print("Your final score: ", current_score)
print("You are ", remainder, " away from the goal")
print(bottom_star_banner)
