# WhileBreak.py
#
# author: Kaoru
# date: 11.08.23

number_of_tries = 3

while True:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!")
        # correct answer, so exit loop with break
        break
    else:
        print("Sorry, that is the wrong answer..."
              "Try again!\n")
        number_of_tries -= 1

        # check number of tries and break if none left        
        if number_of_tries == 0:
            print("You have run out of goes. Sorry.")
            break

x = input("Press any key to exit.")

'''
# assertion test case 1
answer = 42 results in Correct!

# assertion test case 2
ist answer = cat
2nd answer = 42 results in correct!

# assertion test case 3
1st answer = cat
2nd answer = food
3rd answer = sleep results in runout.
'''        
