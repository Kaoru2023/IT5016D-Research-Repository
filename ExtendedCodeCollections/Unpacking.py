# Unpacking.py
#
# author: Kaoru
# date: 29.09.23

items = (1, 2)
print(items)

# unpack values
a, b = (1, 2)
print(a)
print(b)

# anytime you want to ignore a variable, use "underscore" as the variable name
a, _ = (1, 2)
print(a)
# print(b)   # python throws warning if variable is not used, so use _

# if you run this
# a, b, c = (1, 2, 3, 4, 5)  # Python throw error too many values to unpack
# instead, change syntax by using magic " * "
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

# likewise, use _ not to use variable
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
#print(c)


