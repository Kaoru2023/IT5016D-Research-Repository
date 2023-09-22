# Inheritance1.py
#
# author: Kaoru
# date: 05.09.23

class Family: #Parent Class
    def intro(self):
        print("Family introduction")
class Fam1(Family): #Child Class  Fam1 inherits the base class Family
    def position(self):
        print("I am father")
f1 = Fam1()
f1.intro()
f1.position()
