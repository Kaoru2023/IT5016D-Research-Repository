# Gunctions_more_with_arguments_volume_and_area.py
#
# author: Kaoru
# date: 23.08.23


# import and checking directry of math
import math
print(dir(math))

# using an argument and math.pi to calculate the volume of sphare with radius r
def volume(r):
    v = (4.0/3.0) * math.pi * r**3
    print(v)

volume(6)

# assert    user functions are added to dir
print(dir())

# using more arguments to calculate triangle area
# assert print 27
def triangle_area(b,h):
    print(int(0.5 * b * h))

triangle_area(6,9)


