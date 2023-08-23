# L_activities_40List.py
#
# author: Kaoru
# date: 15.08.23

days = 

list_1 = [ 23, 66, 23, 12 ]
list_2 = [ 1,19, 4, 8 ]
combined_list = list_1 + list_2
result_sum = sum(combined_list)
result_average = float(result_sum) / len(combined_list)
user_operation = int()

# assertion output sum 156,average 19.5
#print(result_sum)
#print(result_average)

print("Wecome to sum/avarage generator!\n")
print("List 1", list_1, "List 2", list_2)

# assertion if user input is 1, output 156
# if user output is 2, output 19.5
# included while loop until valid number entered
while user_operation != 1 and user_operation != 2:
    user_operation = int(input("Please choose your operation, 1=sum 2=average:\n"))
    if user_operation == 1:
       print(result_sum)
    elif user_operation == 2:
       print(result_average)
# included error handling
    else:
       print("You entered invalid number")

x = print("Please enter any key to exit")

