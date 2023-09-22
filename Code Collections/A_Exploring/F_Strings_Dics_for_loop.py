# F_Strings.py
#
# author: Kaoru
# date: 14.09.23

# review f string
import math

value = 5.943567

print(f"approximate value = {value:.2f}")  # approximate value = 5.94
print(f"approximate pi = {math.pi:.2f}")   # approximate pi = 3.14

my_car = {'tires': 4, 'doors': 2, 'colour': 'Bayswater', 'seats': 'Leather'}
print(f'My car = {my_car}')  # car = {'tires': 4, 'doors': 2}

address_book = [{'name': 'N.X.', 'addr': '15 Jones St', 'bonus': 70},
                {'name': 'J.P.', 'addr': '1005 5th St', 'bonus': 400},
                {'name': 'A.A.', 'addr': '200001 Bdwy', 'bonus': 5},
                ]

for person in address_book:
    print(f'{person["name"]:5} || {person["addr"]:20} || {person["bonus"]:>5}')

# N.X.     || 15 Jones St          ||    70
# J.P.     || 1005 5th St          ||   400
# A.A.     || 200001 Bdwy          ||     5




