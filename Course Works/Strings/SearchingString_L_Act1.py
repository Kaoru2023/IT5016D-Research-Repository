# SearchingString_L_Act1.py
#
# author: Kaoru
# date: 31.08.23

# This is a program that returns the number of spaces in the string.

# creating function that return space count
def check_space(str):
      count = 0
      for i in range(0, len(str)):
            if str[i] == " ":
                count += 1
      return count

str = "Ka mate kāinga tahi ka ora kāinga rua."
print("The number of spaces appear in the string is:", check_space(str))

# version 2
def check_space(str):
      count = 0
      for i in str:
            if i == " ":
                count += 1
      return count

str = "Ka mate kāinga tahi ka ora kāinga rua."
print("The number of spaces appear in the string is:", check_space(str))