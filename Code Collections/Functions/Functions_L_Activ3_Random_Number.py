# Functions_L_Activ3_Random_Number.py
#
# author: Kaoru
# date: 23.08.23

# This is a program that outputs a random number to the screen every time
#the user types r. If the user types anything else then the program should
#terminate.

import random

def lucky_number():
    print("Your lucky number is {}".format(random.randint(1, 100)))

user_input = input("Enter r to find your lucky number: ")
#"r" = user_input
#this part was hard....

if user_input == "r":
    lucky_number()
else:
    print("Too bad! See you again!")
                                           
    
''' It was hard to figure out the way to desplay a random number.
Many try&errors until finally finding out how to deal with user's input,
letter "r" and bring it to use as a condition'''

# did't realise it will repeat returning while user input "r", so modified
while input("Enter r to find your lucky number: ") == "r":
    lucky_number()
print("Too bad! See you again!")
    
# refine a bit...
def unlucky_number():
    return random.randint(1, 100)

while input("Enter r to find your unlucky number: ") == "r":
    rand_num = unlucky_number()
    print("Your unlucky number is {}".format(rand_num))
print("Too bad! See you again!")

# and refine a bit...
def unlucky_number():
    return random.randint(1, 100)

while input("Enter r to find your unlucky number: ") == "r":
    print("Your unlucky number is {}".format(random.randint(1, 100)))
print("Too bad! See you again!")
