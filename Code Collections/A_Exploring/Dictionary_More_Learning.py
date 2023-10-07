# Dictionary_More_Learning.py
#
# author: Kaoru
# date: 26.09.23
from typing import Dict

customer = {
    "name": "Taro",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

print(customer.get("name"))

print(customer.get("birthdate", "Oct 20 1970"))

''' could not get the expected result
phone_number = {
    1234: "One Two Three Four"
}
print("Phone: ", phone_number.keys(),
      "\n", phone_number.values(),
      )
'''

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for word in phone:
    output += "{0} ".format(digits_mapping.get(word, "!"))
print(output)

print("Welcome to Jp=>En Translator")
j_phrase = input(">")
words = j_phrase.split(" ")
j_e_converter: dict[str, str] = {
    "Bori": "Volley",
    "kawai": "lovely",
    "kotchi": "here",
    "gohan": "kai",
    "oishi": "yummy",
    "oide": "come",
    "tabena": "have"
}
output = ""
for word in words:
    output += j_e_converter.get(word, word) + " "
print(output)

