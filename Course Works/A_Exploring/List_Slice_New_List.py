# List_Slice_New_List.py
#
# author: Kaoru
# date: 14.09.23

# making lists to store a chunk of info
# [name, price, currency, stock, rating]

hdmi_cable = ['HDMI Cable', 9.50, 'NZD', 58, 5.0]
printer = ['Printer', 58.20, 'NZD', 21, 3.75]

# checking the length of list
print(len(hdmi_cable)) # 5

# printing item in the list by specifying the index
print(printer[1]) # 58.28


laptop_product = ["Laptop", 899.00, "NZD", 2, 3.34]
keyboard_product = ["Keyboard", 29.50, "NZD", 6, 4.80]
mouse_product = ["Mouse", 13.99, "NZD", 14, 2.45]

# calcrate average of rating
laptop_rating = laptop_product[4]
keyboard_rating = keyboard_product[4]
mouse_rating = mouse_product[4]
rating_total = laptop_rating + keyboard_rating + mouse_rating
average = rating_total/3
print(average) # 3.53

# create new lists and compute average of inventory pricing # 186.43
keyboard_inventory = [keyboard_product[0], keyboard_product[1], keyboard_product[3], keyboard_product[1] * keyboard_product[3]]
mouse_inventory = [mouse_product[0], mouse_product[1], mouse_product[3], mouse_product[1] * mouse_product[3]]

average_inventory_pricing = (keyboard_inventory[3] + mouse_inventory[3])/2
print(average_inventory_pricing)
