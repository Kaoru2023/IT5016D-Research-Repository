# Decorator_Datetime_Functions.py
#
# author: Kaoru
# date: 25.09.23

from datetime import datetime


def not_during_the_night(func):
    def wrapper():  # define a wrapper function
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass

    return wrapper


def say_whee():
    print("Whee!")


# decorating say_whee by the function not_during _the_night
# this should be called during day, not during night
say_whee = not_during_the_night(say_whee)

print(say_whee())

'''
assertion
output "Whee" if time is 7-22
if not, None

'''