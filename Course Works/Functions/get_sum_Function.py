# get_sum_Function.py
#
# author: Kaoru
# date: 20.09.23

# Create a simple calculator that just sums 2 numbers entered by the user.
# Use the function to return the calculated answer to the calling code.

print("Sum of Your Numbers\n")


def get_sum(num1, num2):
    your_sum = num1 + num2
    return your_sum


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\nThe sum of {0} and {1} is {2}".format(num1, num2, get_sum(num1, num2)))

# new Fstring
print(f"\nThe sum of {num1} and {num2} is "
      f"{get_sum(num1, num2)}")

'''
assertion
input 10 and 15
output 25
'''