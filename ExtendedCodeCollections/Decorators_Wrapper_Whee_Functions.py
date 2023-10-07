# Decorators_Wrapper_Whee_Functions.py
#
# author: Kaoru
# date: 25.09.23

# define a function
def my_decorator(func):  # taking a function as an argument
    def wrapper():  # create another function without an argument
        print("Something is happening before the function is called.")
        func()  # passed in as the argument will then be called
        print("Something is happening after the function is called.")

    return wrapper  # return a function from a function

@my_decorator  # without this @, I have to define say_whee = my_decorator(say_whee)
               # as in line 23
def say_whee():  # define a function that's going to be passed
    print("Whee!")


# defined two functions, the one that's going to decorate the other function
# reassign say_whee, using my_decorator, passing the function say_whee into it
## Re: line 15  if not saying @my_decorator, have to define as follows:
# say_whee = my_decorator(say_whee)  # say_whee be passed into my_decorator, and
# be wrapped between the print statements and get called
# there, and wrapper be returned
print(say_whee)  # <function my_decorator.<locals>.wrapper at 0x0000021A6091C860>
# say_whee is a function, my_decorator is a reference,
# wrapper function say_whee has been set
print(say_whee())
'''
assertion output
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
'''
