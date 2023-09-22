# Factorial_Get_from_Functions.py
#
# author: Kaoru
# date: 20.09.23

print("Get Factorial")


def factorial(number):
    if type(number) is not int or number < 0:
        return None
    elif number == 0:
        return 1

    i = 0
    f = 1
    while i < number:
        i += 1
        f = f * i
    return f


your_number = int(input("\nEnter number to find factorial: "))
print(f"The factorial of your number is {factorial(your_number)}")

'''
assertion
input 6 
output 720

'''


# calling function of itself
def factorial(number):
    if type(number) is not int or number < 0:
        return None
    elif number == 0:
        return 1

    return number * factorial(number - 1)


your_number = int(input("\nEnter number to find factorial: "))
print(f"The factorial of your number is {factorial(your_number)}")

'''
assertion
input 0 and -99
output 1 and "The factorial of your number is None"

'''
