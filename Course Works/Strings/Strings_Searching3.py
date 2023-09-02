# Strings_Searching3.py
#
# author: Kaoru
# date: 31.08.23

# find() function returns only first object. using loop to find duplicates

string = "Taro says 'hai', and Hanako says 'hai', and Jiro says 'hai'."


def number_hai(string):
    count = 0
    while string.find("hai") != -1:
        count += 1
        hai_endindex = string.find("hai") + len("hai")
        string = string[hai_endindex:]
    return count


print(number_hai(string))