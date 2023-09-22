# EAFP_Easier_to_Ask_Forgiveness_than_Permission.py
#
# author: Kaoru
# date: 01.09.23

# Pythonic exception handling approach - try statements

def divide_numbers(number_1, number_2):
    try:
        return number_1/number_2
    except ZeroDivisionError:
        return  "Error, cannot divided by zero!"

# assert - output "Error, cannot divided by zero!"
print(divide_numbers(3,0))

# additional handler can be defined, ex. to handle TypeError.
# Best practice to specify individual handlers for each error type.
# the exception object can be called upon to provide the Python error message,
# "except TypeError as e:"
def divide_numbers(number_3, number_4):
    try:
        return number_3/number_4
    except ZeroDivisionError:
        return "Error, cannot divid by zero."
    except TypeError as e:
        message = "Error, an operand is the wrong type...\n"\
                "Or as Python would say...\n{}".format(e)
        return message

print(divide_numbers(3, "Four"))