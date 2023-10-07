# Volley_Functions_calling_Functions.py
#
# author: Kaoru
# date: 25.09.23

def say_ohayo(name):
    return f"Ohayo {name}"


def say_come_here(name):
    return f"Come here {name}"


print(say_ohayo("Volley"),
      say_come_here("Volley"),
      sep="\n",
      )

# putting functions in a list
my_list = [say_ohayo, say_come_here]
print(my_list)

# calling a function out from a list
print(my_list[0]("Volley"))


# put a function in a function as an argument
# a function can call another function
def greet_volley(greeter_func):
    return greeter_func("Volley")  # plugging Volley as its argument


print(greet_volley(say_ohayo))  # don't need to put an argument in say_ohayo,
print(greet_volley(say_come_here))  # it's going to get from greeter_func
