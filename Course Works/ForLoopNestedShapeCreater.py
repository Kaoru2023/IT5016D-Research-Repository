# ForLoopNestedShapeCreater
#
# author: Kaoru
# date: 14.08.23

print("Welcome to the shape creater!\n")
user_input = int(input("Please enter a number for the size"
                       " of the shape you wish to create.\n"))

for i in range(user_input):
    for j in range(i):
        print('@ ', end="")
    print('')

for i in range(user_input, 0, -1):
    for j in range(i):
        print('@ ', end="")
    print('')

