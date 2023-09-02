# Strings_Searching2.py
#
# author: kaoru
# date: 31.08.23

string_1 = "how do you translate?: gokigen ikaga desuka means how are you!"

# using count function
# assert - output 3
print("The number of times that letter 'g' appears is {}\n"
      .format(string_1.count("g")))

# using find() function. It returns the index integer of the item being searched for.
# assert - output 23, then 30
print("index of the word gokigen is {}\n"
      .format(string_1.find("gokigen")))

gokigen_endindex = string_1.find("gokigen") + len("gokigen")
print("The end index of the word 'gokigen' is {}\n"
      .format(gokigen_endindex))

# <string being searched>.find(<string to search for>, <start index>, <end index>
# the start and end index parameters are optional
# assert - output 50
how_position = string_1.find("how", gokigen_endindex, len(string_1))
print("Looking for the word 'how', anytime after 'gokigen...'\n\n"
      "The word 'how' appears at index position {}.."
      .format(how_position))

# find( ) only returns the first instance of the item being searched for.
# Any duplicates will be ignored.