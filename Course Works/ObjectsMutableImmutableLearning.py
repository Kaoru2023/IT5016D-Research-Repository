# MutableImmutableObjects.py
#
# author: Kaoru
# date: 16.08.23

# Mutable objects "list"
pantry = ['sugar', 'salt', 'peppar', 'flour', 'ice cream' ]
print(pantry)

# checking id of the object
print(id(pantry))

# checking attributes belong to the object
print(dir(pantry))

# using the remove method to remove the last item in the list
# assertion 'ice cream' is removed from the list, and id is still the same
pantry.remove('ice cream')
print(pantry)
print(id(pantry))


# Immutable object "string"
words = "It's a beautiful day."
print(words)
print(id(words))

# concatinating words, assertion output entire phrase
words = words + " Let's go outside!"
print(words)

# checking id of the object, assertion it has different id than the previous object
print(id(words))
