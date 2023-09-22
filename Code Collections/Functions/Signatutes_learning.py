# Signatutes_learning.py
#
# author: Kaoru
# date: 24.08.23

def young_age(my_age):
    print("My age 10 years ago was {0}."
          .format(my_age - 10))

# invoking function
young_age(52)

# if no parameter is given, = missing signature, return an error
'''
def young_age(my_age):
    print("My age 10 years ago was {0}."
          .format(my_age - 10))
young_age()
'''
# trying with two parameters
def young_age(my_age, my_name):
    print("My name is {1}.\n"
          "My age 10 years ago was {0}.\n"
          .format(my_age-10, my_name))
young_age(52, "Kaoru")

