# LearningTuple.py
#
# author: Kaoru
# date: 17.08.23

# Tuples are Immutable

# creating tuple
my_tuple = ("a", "b", "c",1, 2, 3)
print(my_tuple)
print(my_tuple[2])

# checking what can be done for tuple
print(dir(my_tuple))

# assertion - output error when trying to change items in tuple
#my_tuple[2] = "d"

# finding the index of an item in my tuple
# assertion - output 2
index = my_tuple.index("c")
print(index)
