# CelsiusFahrenheitConverter.py
#
# author: Kaoru
# date: 14.08.23

# practice "slice" "if-elif" "string operator"

# program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# C = (5/9) * (F - 32), F = 9C / 5+32
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# if input.upper() == c or f    <== input  degree = int(temp[:-1] , convention = temp[-1]

temp = input("Enter the temperature you want to convert, followed by C or F: ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result = int(round(9 * degree)/5 + 32)
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5/9))
    o_convention = "Celsius"
else:
    print("Enter proper convention.")

print("The temperature in", o_convention, "is", result, "degrees.")



