# RollDice.py
#
# author: Kaoru
# date: 10.08.23

# Craps Roller
# Demonstrates random number genetation

import random

# generate random numbers 1-6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

if total % 2 == 0:
    print("Chou")
else:
    print("Han")
