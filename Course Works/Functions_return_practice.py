# Functions_return_practice.py
#
# author: Kaoru
# date:024.08.23

# more practice for return statement
# create a simple calc programe

def get_multiply(x, y):
    result = x * y
    return result

#print statement to see the result
print(get_multiply(3,6))

# an alternative
def get_multiply2(a,b):
    return a * b

print(get_multiply2(2, 4))

# store as a variable
def get_multiply3(c,d):
    return c * d

z = get_multiply3(5,7)

print(z)
