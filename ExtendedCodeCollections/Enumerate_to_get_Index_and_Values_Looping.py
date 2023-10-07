# Enumerate_to_get_Index_and_Values_Looping.py
#
# author: Kaoru
# date: 29.09.23

# to get index and item in the list...
names = ['Miko', 'Bubbles', 'Poki', 'Pui', 'Munk']

index = 0
for name in names:
    print(index, name)
    index += 1

# use Enumerate Function to get index and value while looping
for index, name in enumerate(names):
    print(index, name)

# you can specify to start value, like 1 if you want to start with 1
for index, name in enumerate(names, start=1):
    print(index, name)