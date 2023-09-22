# StringLengthTest.py
#
# autor: kaoru
# 10.08.23

# This is to check the length of user password
# set to string version
input_password = str(input("Please enter password: "))
if len(input_password) < 6:
    print("characters needs to be at least 6")
else:
    print("password confirmed")

# raw_input version
# did not work in Python 3
# error name, 'raw_input' is not defined
# input_password = raw_input("Please enter password\n")
# if len(input_password) < 10:
#    print("characters needs to be at least 10")
# else:
#    print("enter again to confirm")
