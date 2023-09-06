# IteratingLists.py
#
# author: Kaoru
# date: 15.08.23

# Iterating is a mean loop through a list. Learning the for-in structure

sample_list = [1,4,5,2,9,12]

for i in sample_list:
    print("An i in the sample listt is ", i)

# using the enumerate function to get the index and the item
for index, i in enumerate(sample_list):
    print("The element index is ",index," and the value is ", i)

# using range and len to get the index only
for index in range(len(sample_list)):
    print("The element index is ",index)

# The list object supports the iterator protocol. To explicitly
# cretae an iterator, use the built-in iter function:

i = iter(sample_list)
item = i.__next__() # fetch first value
print("An item in the sample list is ", item)
item = i.__next__() # fetch second value
print("An item in the sample list is ", item)

# using Python's various shortcuts for common list operations.
# if a list contains numbers, the built-in sum function gives sum:

list_sum = sum(sample_list)
print("\nThe sum of the items in the list is...", list_sum)

subtotal = 23
total = sum(sample_list, subtotal)
print("\nThe sum of the items in the list and another number is...", total)

average = float(sum(sample_list)) / len(sample_list)
print("\nThe average of the items in the list is...", average)

# using the join string method to combine the string into a single long string
# assertion output JyugemyJyugemu ponpoko rin no
jyugemu_list = ["Jyugemu""Jyugemu","ponpoko","rin","no"]
joined_list = " ".join(jyugemu_list)
print("\nYour name is...", joined_list)
