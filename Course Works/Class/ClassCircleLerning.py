# LerningClassCircle.py
#
# author: Kaoru
# date: 16.08.23

# write a programe to create a class representing a Circle.
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius**2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius


# interacting users
radius = float(input("Enter the radius of the circle: \n"))
circle = Circle(radius)
area = circle.calculate_circle_area() 
perimeter = circle.calculate_circle_perimeter()
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)
'''


import math
class Circle2:
    def __init__(self):
        self.radius = None
    def set_radius(self, radius):
        self.radius = radius

    def cal_area(self):
        return math.pi * self.radius**2

    def cal_perimeter(self):
        return 2 * math.pi * self.radius


circleK = Circle2()
circleL = Circle2()

circleK.set_radius(5)
print("The area of the circle is", circleK.cal_area())






        
        
    
