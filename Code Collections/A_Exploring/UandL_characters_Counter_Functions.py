# UandL_characters_Counter_Functions.py
#
# author: Kaoru
# date: 20.09.23

# Finding the number of upper case and lower case characters + spaces and other characters

print("\nCounting Characters\n")
word = input("Please enter phrases: ")


def get_count(word):
    upper_count, lower_count, space_count, other_count = 0, 0, 0, 0
    for key, value in enumerate(word):
        if value.isupper():
            upper_count += 1
        elif value.islower():
            lower_count += 1
        elif value.isspace():
            space_count += 1
        else:
            other_count += 1
    return {"Upper case characters": upper_count,
            "Lower case characters": lower_count,
            "Spaces": space_count,
            "Other characters": other_count,
            }


print("\nCharacter Counts:\n")
counter_dict = get_count(word)
for key, value in counter_dict.items():
    # replacing ',' to ':' and remove ' as it looks better when printing
    print(f"{key, value}".replace(",",":").replace("'",""))

'''
assertion

input
I am learning Python! In a few months, I can write any Python code more freely and comfortably!!!!

output
('Upper case characters': 5)
('Lower case characters': 70)
('Spaces': 17)
('Other characters': 6)
'''