# Max_num_Get_Data_from_Functions.py
#
# author: Kaoru
# date: 20.09.23

# finding the max number of 3 stored numbers

print("Find the Max Number")

num_list = []


def get_numbers(num_list):
    counter = len(num_list)
    while counter < 3:
        input_numbers = int(input("Please enter a number: "))
        num_list.append(input_numbers)
        counter += 1
    return num_list


def get_max_number(num_list):
    max_number = num_list[0]
    counter = 1
    while counter < len(num_list):
        if num_list[counter] > max_number:
            max_number = num_list[counter]
        counter += 1
    return max_number

num_list = get_numbers([])
print("\n{0} is the max number of your numbers:{1}"
      .format(get_max_number(num_list), num_list))

'''

assertion

input 159, 231, 0

output
Please enter a number: 159
Please enter a number: 231
Please enter a number: 0

231 is the max number of your numbers:[159, 231, 0]

'''
