# RepetitiveMessageDisplayer.py
#
# author: Kaoru
# date: 14.08.23

# This programe is to display message the number of times that a user wants.

print("\nWelcome to message displayer!\n")

message = input("Please enter your message...\n")
                
number = int(input("Please enter the number of times "
                   "that you wish to desplay your message.\n"))


for i in range(number):
    print(message)

# adding the bit to display the number of thimes...

    print("message...", i)

# not quite right...try again

    print(message,"...", i)

print("\nWelcome to message displayer!\n")

message = input("Please enter your message...\n")
                
number = int(input("Please enter the number of times "
                   "that you wish to desplay your message.\n"))

for i in range(number):
    print(message,"...", i)
