# RepetitiveMessageDisplayer.py
#
# author: Kaoru
# date: 14.08.23

# This program is to display message the number of times that a user wants.

print("\nWelcome to message displayer!\n")

message = input("Please enter your message...\n")
                
number = int(input("Please enter the number of times "
                   "that you wish to display your message.\n"))


for i in range(number):
    print(message)

# adding the bit to display the number of times...

    print("message...", i)

# not quite right...try again

    print(message,"...", i)

#
print("\nWelcome to message displayer!\n")

message = input("Please enter your message...\n")
                
number = int(input("Please enter the number of times "
                   "that you wish to display your message.\n"))

for i in range(number):
    print(message,"...", i)

# changing counter
    print(message,"...", i + 1)