# ParkingCul.py
#
# autor: Kaoru
# 10.08.23

print("Kis Ora. This is a parking meter.")
park_time = 6
print("park time is", park_time, "hours.")

rate = 4
cost = 0

if park_time > 3:
    cost = rate * 3
    # reducing rate
    rate -= 2
    # getting reminder of the parking park_time
    park_time -= 3
    # add the current cost
    cost += rate * park_time
    print("The cost of parking is $", cost)
else:
    cost = rate * park_time
    print("The cost of parking is $", cost)

# assertion
'''
The cost of parking should be $18
'''

# usually you do not enter parking time yourself, but just playing around
#making an interactive version

print("Kia Ora, this is a parking meter")
park_time = int(input("Please enter your park time\n"))
print("park time is", park_time, "hours.")

rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    # drop the rate by $2
    rate -= 2
    # get the reminder of the parking park_time
    park_time -= 3
    # add the current cost
    cost += rate * park_time
# concatenating $ and number to remove space
# showing price with two decimal numbers
    print("The cost of the parking is $" + '{0:.2f}'.format(cost))
else:
    cost = rate * park_time
    print("The cost of the parking is $" + '(0:.2f)'.format(cost))
    
