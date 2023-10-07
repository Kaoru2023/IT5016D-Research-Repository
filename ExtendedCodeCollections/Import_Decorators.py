# Import_Decorators.py
#
# author: Kaoru
# date: 25.09.23

from Decorators import *


@do_twice
def say_whee():
    print("Whee!")


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


print(waste_some_time(999))
