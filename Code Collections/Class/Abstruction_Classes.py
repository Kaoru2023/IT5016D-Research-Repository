# Abstruction_Classes.py
#
# author: Kaoru
# date: 05.09.23

from abc import ABC
class Person(ABC):
    # abstruct method
    def occupation(self):
        pass
class Student(Person):
        def occupation(self):
            print("I am student")
class Teacher(Person):
        def occupation(self):
            print("I am teacher")
class Manager(Person):
        def occupation(self):
            print("I am manager")

    # driver code
s = Student()
s.occupation()

t = Teacher()
t.occupation()

m = Manager()
m.occupation()

