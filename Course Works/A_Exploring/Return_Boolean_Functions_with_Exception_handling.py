# Return_Boolean_Functions_with_Exception_handling.py
#
# author: Kaoru
# date: 20.09.23

# This is a program return True if the taken first number is within the range
# between second and third number, otherwise return False.

print("\nFinding if first number is between the second and third numbers\n")

num_list = []


def get_numbers(num_list):
    counter = len(num_list)
    while counter < 3:
        try:
            number = float(input("Please enter a number:"))
            if number.is_integer():
                number = int(number)
            num_list.append(number)
            counter += 1
        except ValueError:
            print("Wrong input. Please enter a number ...")
    return num_list


def get_bool(num_list):
    if num_list[2] > num_list[1]:
        if num_list[1] <= num_list[0] <= num_list[2]:
            return True
        else:
            return False
    else:
        if num_list[1] >= num_list[0] >= num_list[2]:
            return True
        else:
            return False

num_list = get_numbers([])
print("\nIt is {0} that {1} is within the range of {2} and {3}."
      .format(str(get_bool(num_list)).lower(),
              num_list[0],
              num_list[1],
              num_list[2]))

'''
assertion
input 1,2,3 output "It is false that 1 is within the range of 2 and 3."

input 9.8, 2, 6.7
output "It is false that 9.8 is within the range of 2 and 6.7."

input nine
output "Wrong input. Please enter a number ...
Please enter a number:"
'''








