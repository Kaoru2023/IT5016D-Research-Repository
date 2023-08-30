# ParkingCal_usingFunction_Return.py
#
# author: Kaoru
# date: 24.08.23

'''
This task is repeated from earlier in the course. Write more concise code using a function with
a return statement.
A parking meter charges $4 for the first 2 hours, then $3 for every hour thereafter.
Write a program that displays a welcome message and instructions, then prompts the user for
the number of hours that they need to park. The program should display the calculated cost of
parking.
'''


def get_park_charge(hours):
    rate = 4
    cost = 0
    if hours >= 3:
        cost = rate * 2
        # reducing rate
        rate -= 1
        # getting reminder of hours
        hours -= 2
        # add the current cost
        cost += rate * hours
        return cost
    else:
        return rate * hours
# assert - print 8
print(get_park_charge(2))

# assert - print 20
print(get_park_charge(6))