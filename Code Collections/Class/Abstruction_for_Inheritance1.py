# Abstruction_for_Inheritance1.py
#
# author: Kaoru
# date: 05.09.23

from abc import ABC
class Family(ABC):
    def position(self):
        pass
class Father(Family):
    def position(self):
        print("I am father")
class Mother(Family):
    def position(self):
        print("I am mother")
class Daughter(Family):
    def position(self):
        print("I am daughter")
class Son(Family):
    def position(self):
        print("I am son")
f = Father()
f.position()

m = Mother()
m.position()

d = Daughter()
d.position()

s = Son()
s.position()