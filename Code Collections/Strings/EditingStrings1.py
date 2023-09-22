# EditingStrings.py
#
# author: Kaoru
# date: 31.08.23

#Replacing part of a string with a new variable value.
string_1 = "Hello World."
print("Replacing part of string...{}\n"
      .format(string_1.replace('Hello','Goodbye')))

#replace()function can take upto 3 parameters.
#passing count parameter to define number of replacement
string_2 = "Hello World, Hello Flowers, Hello Birds."
print("Replacing the first two Hello with Goodbye..{}"
      .format(string_2.replace("Hello","Goodbye",2)))

#making string Upper case
string_3 = "HellO WorlD"
print("making string upper case...{}\n"
      .format(string_3.upper()))
print(string_3.upper())
#making string Lower case
print("making string lower case...{}\n"
      .format(string_3.lower()))
print(string_3.lower())
#making string Title case
print("making string title case...{}\n"
      .format(string_3.title()))
#making string capitalise
print("making string capitalise...{}\n"
      .format(string_3.capitalize()))
#making string Swap case
print("making string swap case...{}\n"
      .format(string_3.swapcase()))
#reversing and inserting characters to string
print("Reversing and inserting characters to a string...\n{0}"
      .format("*".join(reversed(string_3))),
      "\n")
#concatenating using + operator
string_4 = "Hello"+"World"

print("Using the join method to add a : between every char...\n{0}"
      .format(":".join(string_4)),
      "\n")

print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_4)),
      "\n")

#sprit The simplest use of the split function takes no arguments and
#splits a string on white spaces, to return a list of strings.
#White space is the default delimiter.
string_5 = "It's only after we've lost everything " \
           "that we're free to do anything"
print("Splitting string by default delimiter...{}\n"
      .format(string_5.split()))
#split( ) also has an optional single string argument to set
#the delimiter character/s instead.
print("Splitting string by default delimiter...{}\n"
      .format(string_5.split("e")))