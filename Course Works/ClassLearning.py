# LearningClass.py
#
# author: Kaoru
# date: 16.08.23


class Vehicle: # Parent Vehicle class

    def __init__(self, colour, make):
        self.colour = colour
        self.make = make
        self.fuel = 4 # a full tank of fuel

    def drive(self): # adding a method - when call this method, output "Vroom"
                     # loop 4 times and then print "sputter" at 5th try
        if self.fuel > 0:
            self.fuel -= 1
            print("The {} {} goes Vroom".format(self.colour, self.make))
        else:
            print("The {} {} sputters out of fuel.".format(self.colour, self.make))

class Car(Vehicle): # Subclass Inherits from Vehicle class

    # adding a method - turn the music on
    def music(self):
        print("It's a beautiful day....")

    # adding a method - put seat heater
    def seat(self):
        print("Nice and warm!")

class Motorcycle(Vehicle): # Inherits from Vehicle

    # adding a method - put on leather jacket
    def jacket(self):
        print("Ready to go!")

my_car = Car("Bayswater","Mini")   
my_mc = Motorcycle("Black","Kawasaki")
my_car.drive() # calling drive method
my_car.drive()
my_car.drive()
my_car.drive()
my_car.drive() # output "sputters" with if loop
my_mc.drive() # ride motorcycle instead
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive() # output "sputters" with if loop

my_car.music()
my_car.seat()

my_mc.jacket()

my_mc.seat() # assertion output error - Motorcycle object does not have attribute 'seat'
