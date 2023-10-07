# Decorators.py
#
# author: Kaoru
# date: 25.09.23

import functools
import time


# create template
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice



def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value

    return wrapper_decorator

# copy template
def timer(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # do something before
        value = func(*args, **kwargs)
        end_time = time.perf_counter()   # do something after
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
