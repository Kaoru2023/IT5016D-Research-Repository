# Functions_L_Activ2.py
#
# author: Kaoru
# date: 23.08.23

# ThiS iS a program that stores an integer value x and a string of value y
#(you can choose these values). The program must use a method that displays
# the y text, x number of times.

def print_message(x, y):
    print(y * x)


y = input("Enter your message: \n")
x = int(input("Repeating...: \n"))
print_message(x, y)


'''First, I had no idea how I can make this program. It was a little surprise
to see "print(y * x)" worked!'''

# Now trying loop

def print_message2(x, y):
    for i in range(1,x):
        print(y, end='')

y = input("Enter your message: \n")
x = int(input("Repeating...: \n"))
print_message2(x, y)
