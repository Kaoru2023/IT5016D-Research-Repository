# List_Changing.py
#
# authod: Kaoru
# date: 17.08.23

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

# Adds a single element to the end of list_1
list_1.append(9)
print(list_1)

# appends all of list_2 elements to the end of list_1
list_1.extend(list_2)
print(list_1)

# insert the element at the given index, shifting elements to the right
# inserting 10 after 4
list_1.insert(4, 10)
print(list_1)

# search for the given element from the start of the list and return its index
print(list_1.index(7))

# remove the first given element in the list
print(list_1.remove(1))
print(list_1)

# reverse the list
list_1.reverse()
print(list_1)

# remove and return the element at the given index
list_1.pop(0)
print(list_1)

# a boolean check if a value exist in the list
if 25 in list_1:
    print(True)
else:
    print(False)
    
    



