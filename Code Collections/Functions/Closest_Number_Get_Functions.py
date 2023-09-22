# Closest_Number_Get_Functions.py
#
# author: Kaoru
# date: 20.09.23

# return the closest number in the list to the number input

print("Find the closest number")

number_list = [60, 70, 178]
user_number = float(input("Enter a number: "))
if user_number.is_integer():
    user_number = int(user_number)

def get_closest(user_number, number_list):
    counter = 1
    closest = number_list[0]
    diffs = abs(number_list[0] - user_number)
    while counter < len(number_list):
        nDiffs = abs(number_list[counter] - user_number)
        if nDiffs < diffs:
            diffs = nDiffs
            closest = number_list[counter]
        counter += 1
    return closest

print(f"\nList of numbers to compare with {number_list}"
      f"\n{user_number} is closest to {get_closest(user_number,number_list)}")

'''
assertion
input 65.5 
closest number 70
'''
