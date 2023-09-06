# ListsPractice.py
#
# author: Kaoru
# date: 15.08.23

# The python list is a data type

#L = []
#L = [expression, ...]


#L = list() # empty list
#L = list(sequence)


#A = B =[1,2] #both names will point to the same list

#A = []

#B = A #both names will point to the same list

#A = []; B = [] #independent lists

#len(L) #returnes the number of items in the list

#L[i] #returns the item at index i (the first item has index 0)

#L[i:j] #returns a new list, containing the objects between i and j.

#n = len(L)

#item = L[index]

my_list = []
# list of integers
my_list = [1, 2, 3]

# checking type of my_list
print(type(my_list))

# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)

# nested list
my_list = ["mouse", [8, 4, 6]]
print(my_list)

my_list = ['p', 'r', 'o', 'e', 'b']
# output: o
# print(my_list[3]) wrong
print(my_list[2]) #correct - 0,1,2
# print(my_list[5]) out of range error

# my_list[4.0]
# print(my_list) only integer can be used for indexing

# Nested List
n_list = ["Happy", [3,2,1,0]]
# output first y, then H, then 2, then 0
print(n_list[0][4])
print(n_list[0][0])
print(n_list[1][1])
print(n_list[1][3])

# using negative indexing
# output first b, then p
print(my_list[-1])
print(my_list[-5])

# slicing    print r,o,e
print(my_list[1:4])

#combining lists = concatenation *orders matter
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)
print(letters + numbers)

print(dir(numbers))
print(help(numbers.reverse))







