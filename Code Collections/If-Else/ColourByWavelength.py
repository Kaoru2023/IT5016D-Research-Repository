# ColourByWavelength
#
# autor: Kaoru
# date: 10.08.23

# pragrame to reports colour by reading a wavelength enter by users

# my version
wavelength = int(input("Please enter Wavelength\n"))

if wavelength < 750 and wavelength > 620:
    print("Red")
elif wavelength < 620 and wavelength > 590:
    print("Orange")
elif wavelength < 590 and wavelength > 570:
    print("Yellow")
elif wavelength < 570 and wavelength > 495:
    print("Green")
elif wavelength < 495 and wavelength > 450:
    print("Blue")
elif wavelength < 450 and wavelength > 380:
    print("Violet")
else:
    print("Please enter valid value")

# textbook version
print("Welcome to wavelength to colour converter\n")
wave_length = int(input("Please enter an integer wavelength between 380 and 750\n"))
print("Thank you, the wavelength that you enter in nanometer is ", wave_length,"\n")
print("The colour for this wavelength is...", end="")

if wave_length > 750:
    print("The wanelength entered is higher than the visible spectrum! This is infrared.")
elif wave_length > 620:
    print("Red")
elif wave_length > 590:
    print("Orange")
elif wave_length > 570:
    print("Yellow")
elif wave_length > 495:
    print("Green")
elif wave_length > 450:
    print("Blue")
elif wave_length > 380:
    print("Violet")
else:
    print("Indeterminate, :-(, the number entered is"
          "outside the visible spectrum!")

# test case assersion 1
'''

wave_length = 720
colour is Red
'''
    
