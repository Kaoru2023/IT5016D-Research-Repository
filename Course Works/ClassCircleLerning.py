# LerningClassCircle.py
#
# author: Kaoru
# date: 16.08.23

# write a programe to create a class representing a Circle.

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

        
        
    
