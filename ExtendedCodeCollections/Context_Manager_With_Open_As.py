# Context_Manager_With_Open_As.py
#
# author: Kaoru
# date: 29.09.23

# have to close after open a file like...

f = open("test.txt", "r")
file_contents = f.read()
f.close()  # close file each time like this ???

words = file_contents.split(" ")
word_count = len(words)
print(word_count)

# instead, Context Manager can take care of it
with open("test.txt", "r") as f:
    file_contents = f.read()

words = file_contents.split(" ")
word_count = len(words)
print(word_count)
