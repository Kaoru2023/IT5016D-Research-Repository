# Experiment_self_parameter.py
#
# author: Kaoru
# date: 05.09.23

# using a different name instead of 'self' to call the self-parameter
class Animal:
        def __init__(animal, colour, age):
            animal.colour = colour
            animal.age = age

        def intro(animal):
            print('My colour is ' + animal.colour)
            print('My age is ', animal.age)

catA = Animal('black',5)
catB = Animal('white',3)

catA.intro()
catB.intro()

# updating the value of object(instance)
# altering catA age
catA.age = 6
catA.intro()

# deleting value from object
del catB.age
catB.intro()
