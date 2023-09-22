# Function_required_arguments_and_keyword_arguments.py
#
# author: kaoru
# date: 23.08.23

# Keyword arguments, also called default arguments must come last
# Required arguments must come first

# assert  return error
'''def g(x = 0, y):
    print(x + y)

g'''

# fixing
def g(y, x = 0):
    print(x + y)

# can go without specifying default argument
g(5)

# need to specify default argument as follows
g(5, x = 5)
    
