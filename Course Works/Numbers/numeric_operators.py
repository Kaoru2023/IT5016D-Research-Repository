# numeric_operators.py
#
# autor: Administrator
# 08.08.23

# finding the area of any square with a side length of j. There are no units needed

side_j = int(input("Please enter the length of the square\n\n"))
print("\nThe area of your square is ", side_j ** 2,"n\n")

#Testing
'''
print("My assertions are:
      "\nj = 5 output = 25"
      "\nj = 12 output = 144"
'''

# outputting the area of a compound shape with dimentions that user input
# getting user inputs
a = int(input("Please enter the length of a\n"))
b = int(input("Please enter the length of b\n"))

# working out the 2 parts
total_area = b * a + a ** 2
print("The total area of your shape is ",total_area, "\n")

#Testing
'''
print("My assertions are:
      "\na = 5, b = 10 output 75"
      "\na = 6, b = 15 output 126")
'''

