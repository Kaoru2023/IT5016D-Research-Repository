# Strings_Searching4.py
#
# author: Kaoru
# date: 31.08.23

# more examples of search functions
# The starts with and ends with functions return boolean.
# assert - output True, False, then True
string_1 = "Ka mate kāinga tahi ka ora kāinga rua."

print("Does this string start with 'Ka'?..{}\n"
      .format(string_1.startswith("Ka")))
print("Does this string start with 'Rua'?..{}\n"
      .format(string_1.startswith("Rua")))
print("Does this string end with 'rua'?..{}\n"
      .format(string_1.endswith("rua.")))

# Other functions used with strings include:
string_2 = "kāinga"
print(string_2.isalnum())         #check if all char are alphanumeric
print(string_2.isalpha())         #check if all char in the string are alphabetic
print(string_2.isdigit())         #test if string contains digits
print(string_2.istitle())         #test if string contains title words
print(string_2.isupper())        #test if string contains upper case
print(string_2.islower())         #test if string contains lower case
print(string_2.isspace())         #test if string contains spaces