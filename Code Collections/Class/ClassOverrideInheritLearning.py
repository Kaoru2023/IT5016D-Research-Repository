# LearningClassOverridesInherit.py
#
# author: Kaoru
# date: 16.08.23

class Vehicle: # Base Vehicle class

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

class Car(Vehicle): # Inherits from Vehicle class

    # adding a method - turn the music on
    def music(self):
        print("It's a beautiful day....")

    # adding a method - put seat heater
    def seat(self):
        print("Nice and warm!")

class ECar(Car): # Inherits from Car class
    def drive(self): # overrides the drive method
            print("The {} {} goes ssshhh".format(self.colour, self.make))

my_ecar = ECar("Eco","Mini")
my_ecar.music()
my_ecar.seat()
my_ecar.drive()
