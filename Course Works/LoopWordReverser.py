# LoopWordReverser.py
#
# authod: Kaoru
# date: 15.08.23

print("Welcome to word reverser!\n")
# assertion input "!wow wow wow?" output "?wow wow wow!",then "wwwwww?"
# assertion input "abcdefghijklmnop", then output "omkigeca"
word = input("Input a word to reverse: ")

for char in range(len(word) -1, -1, -1):
    print(word[char], end="")
print("\n")

for char in range(len(word) -2, -2, -2):
    print(word[char], end="")
print("\n")

