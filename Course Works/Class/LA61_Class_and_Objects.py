#  LA61_Class_and_Objects.py
#
# author: Kaoru
# date: 05.09.23

class Person:
    def __init__(self, age, gender, address, height):
        self.age = age
        self.gender = gender
        self.address = address
        self.height = height

    def my_intro(self):
        print('my age is ', self.age)
        print('my gender is ' + self.gender)
        print('my address is ' + self.address)
        print('my height is ', self.height)

harry = Person(25,'male','13 Newton Road',175)
marie = Person(23,'female','15 Queen Street',180)

harry.my_intro()

