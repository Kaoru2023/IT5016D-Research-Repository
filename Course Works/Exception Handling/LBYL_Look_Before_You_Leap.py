# LBYL_Look_Before_You_Leap.py
#
# author: Kaoru
# date: 01.09.23

# Exception handling using if statement
def divide_numbers(number_1, number_2):
    if number_2 == 0:
        return "Cannot divided by zero."
    return number_1/number_2
print(divide_numbers(3,0))

