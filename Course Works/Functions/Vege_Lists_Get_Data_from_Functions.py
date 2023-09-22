# Vege_Lists_Get_Data_from_Functions.py
#
# author: Kaoru
# date: 20.09.23

# This is a program using a stored list of three lists which contain veges items.
# If the items in each list is less than 3, ask user to add items until it gets 3.

print("Veges lists")

list_a = ["Cabbage", "Spinach"]
list_b = ["Carrots", "Raddish"]
list_c = ["Broccoli"]
veges_list = [list_a, list_b, list_c]


def get_more_vegetable(vegetable_list):
    count = len(vegetable_list)
    while count < 3:
        vegetable = input(f"Please enter another veges in the list: "
                          f"{vegetable_list}")
        count += 1
        vegetable_list.append(vegetable)
    return vegetable_list


for each_list in veges_list:
    get_more_vegetable(each_list)

print("\nThe 3 vege lists are:")
for each_list in veges_list:
    print(each_list)

'''
assertion

Veges lists
Please enter another veges in the list: ['Cabbage', 'Spinach'] Zucchini
Please enter another veges in the list: ['Carrots', 'Raddish'] Cauliflower
Please enter another veges in the list: ['Broccoli'] Red Onion
Please enter another veges in the list: ['Broccoli', ' Red Onion'] Capsicum

The 3 vege lists are:
['Cabbage', 'Spinach', ' Zucchini']
['Carrots', 'Raddish', ' Caouliflower']
['Broccoli', ' Red Onion', ' Capsicum']

'''