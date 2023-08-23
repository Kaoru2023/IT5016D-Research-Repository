# Functions_define_keyword_arguments_feet_cm_converter.py
#
# author: Kaoru
# date: 23.08.23

def cm(feet = 0, inches = 0):
    '''converts a length from feet and inches to centimeters.'''
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    print(inches_to_cm + feet_to_cm)

# assert print 152.4
cm(feet = 5)

# assert print 177.8
cm(inches = 70)

# assert print 172.72
cm(feet = 5, inches = 8)

# assert print 172.72
cm(inches = 8, feet = 5)
