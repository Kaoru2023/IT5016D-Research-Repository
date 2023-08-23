# TriangleType.py
#
# author: Kaoru
# date: 10.08.23

side_a = int(input("Enter the length of side a\n"))
side_b = int(input("Enter the length of side b\n"))
side_c = int(input("Enter the length of side c\n"))

if side_a == side_b == side_c:
    print("It is an equilateral triangle")
elif (side_a == side_b
      or side_a == side_c
      or side_b == side_c):
    print("It is an isosceles triangle")
else:
    print("It is scalene")
    
