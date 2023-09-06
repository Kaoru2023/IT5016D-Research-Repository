# Class_Access_Modifiers.py
#
# author: Kaoru
# date: 05.09.23

# Public data member: Accessible anywhere from outside of the class
# Private data member: Accessible within the class
# Protected data member: Accessible within the class and its sub_class

class Student:
    #constructor
    def __init__(self, name, section, address):
        # public data member
        self.name = name
        # protected data member
        self._section = section
        # private data member
        self.__address = address
    def get_address(self):
        return self.__address

    # setter method
    def set_address(self, address):
        self.__address = address

s = Student('Taro', 'B','13 Newton Rd')
print("My name is", s.name)
print("My section is", s._section)
print("My address is", s.get_address())

s.set_address("13 Queen Street")

print("My new address is", s.get_address())