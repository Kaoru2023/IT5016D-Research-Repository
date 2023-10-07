# Zip_instead_0f_Enumerate.py
#
# author: Kaoru
# date: 29.09.23

# Enumerate_to_get_Index_and_Values_Looping.py used Enumerate to get both index and value
# while looping
# Here, there are two lists and want to get index and value from each list
# with enumerate...???
names = ['Miko', 'Bubbles', 'Poki', 'Pui', 'Munk']
characters = ['boy but first girl', 'mother', 'first boy', 'cute as girl but boy', 'youngest girl']
colours = ['ginger', 'black and white', 'grey and white with stripy tail', 'black and white like mum', 'grey']

for index, name in enumerate(names):
    character = characters[index]
    print(f"{name} is actually {character}")

# more intuitive Pythonic way, use Zip Function
# allow you loop over two lists at once
for name, character in zip(names, characters):  # put lists want to loop over
    print(f"{name} is actually {character}")

# Zip can be used for more than 2 lists
for name, character, colour in zip(names, characters, colours):  # put lists want to loop over
    print(f"{name} is actually {character} in {colour}")

# Zip can return individual tuple of values
for value in zip(names, characters, colours):
    print(value)


# dou
# yatte
# comment/uncomment
# ippen ni suruno === Ctrl+/