# ClassPractice.py
#
# # author: Kaoru
# date: 05.09.23

class Animal:
    colour = "black"
    gender = "male"

# creating instances(objects) of the Animal class

catA = Animal()
catB = Animal()

# output : black
print(catA.colour)
print(catB.colour)

# using building function __init__
class Animal:
    def __init__(self, colour, gender):
        self.colour = colour
        self.gender = gender
catA = Animal('black', 'male')
catB = Animal('white', 'female')

print(catA.colour)
print(catA.gender)
print(catB.colour)
print(catB.gender)


