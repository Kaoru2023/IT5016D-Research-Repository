# Methods_ClassPractice2.py
#
# author: Kaoru
# date: 05.09.23

# Methods are functions of objects(instance)
# creating a method in the Animal class

class Animal:
    def __init__(self, colour, gender, age):
        self.colour = colour
        self.gender = gender
        self.age = age
    def intro(self):
        print("My colour is " + self.colour)
        print("My gender is " + self.gender)
        # assertion - return TypeError
        #print("my age is " + self.age)
        print("My age is ", self.age)

catA = Animal('black','male',5)
catB = Animal('white','female',3)

catA.intro()
catB.intro()