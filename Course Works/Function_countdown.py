# Functions_countdown.py
#
# author: Kaoru
# date: 24.08.23
import time

def get_seconds(seconds):
    for i in range(seconds,-1,-1):
        time.sleep(1)
        print(i)

print("Welcome to countdown timer!\n")
seconds = int(input("Please enter the number of seconds to countdown..."))
get_seconds(seconds)
print("Happy Birthday")

# playing around a bit....
def get_seconds(seconds,is_print):
    for i in range(seconds,-1,-1):
        time.sleep(1)
        if is_print == True:
            print(i)

print("Welcome to countdown timer!\n")
seconds = int(input("Please enter the number of seconds to countdown..."))
get_seconds(seconds, False)
print("Happy Birthday")
