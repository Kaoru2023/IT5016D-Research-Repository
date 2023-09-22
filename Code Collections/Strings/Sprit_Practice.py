# Sprit_Practice.py
#
# author: Kaoru
# date: 31.08.23

# This is a program that takes a single user input of 3 integers separated by commas
# and then outputs the average of the numbers.

def get_average(user_input):
    splitted_data = user_input.split(",")
#    print(splitted_data)
    int_list = [int(i) for i in splitted_data]
#    print(int_list)
    return sum(splitted_data)/3

user_input = input("Input three numbers separated by a comma")
result = get_average(user_input)
print("The average is :", result)
