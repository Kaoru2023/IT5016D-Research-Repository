# Numbers_Operators.py
#
# author: Kaoru
# date: 26.09.23

numbers = [3, 9, 65, 4, 1864, 555, 392781, 2, 456, 4982]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

numbers.append(6)
print(numbers)

numbers.insert(0, 1)
print(numbers)

numbers.remove(6)
print(numbers)

numbers.pop(0)
print(numbers)

print(555 in numbers)
print(numbers.index(555))

numbers.append(9)
print(numbers.count(9))

numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()

numbers.clear()
print(numbers)

print(numbers2)

'''
dup_number = [0]
for number in numbers2:
    if number == dup_number:
        dup_number = number
        numbers2.remove(dup_number)
print(numbers2)
'''

uniques = []
for number in numbers2:
    if number not in uniques:
        uniques.append(number)

print(uniques)


