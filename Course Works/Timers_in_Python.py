# Timers_in_Python.py
#
# author: Kaoru
# date: 19.08.23

# When the program runs it prints to the console every second.
# It uses a timedelta object called period, and this is set to one second.
# "next_time" is created for some time in the future.
# In the while loop, "next_time" variable is constantly evaluated.
# When the current time passes "next_time", then the print statement and
# any other logic is executed. At the end of the while loop, the loop counter
# is incremented, and "next_time" variable is reset to a new time.
# The looping countinues until the counter reaches its limit,
# then the while statement is exited.

from datetime import datetime, timedelta

duration = 5

run = input("Enter s to begin...")

period = timedelta(seconds=1)

next_time = datetime.now() + period

counter = 0
while run == 's' and counter < duration:
    if next_time <= datetime.now():
        print("..", counter)
        counter += 1
        # reevaluate the next_time variable
        next_time += period


# Creating Count Up and Down Timer, importing time module,  

import time

running = True

seconds = 0

end = 10

while(running):
    print(seconds)
    time.sleep(1)
    seconds += 1
    if(seconds >= end):
        running = False
        print(seconds)
print("Done!")

# Now, counting down

running = True

seconds = 10

end = 0

while(running):
    print(seconds)
    time.sleep(1)
    seconds -= 1
    if(seconds <= end):
        running = False
        print(seconds)
print("Happy New Year!")

# Count Up and Down with for loop

for seconds in range(0,10,+1):
    print(seconds)
    time.sleep(1)
    
print("Done!")

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
    
print("Happy Birthday!")
