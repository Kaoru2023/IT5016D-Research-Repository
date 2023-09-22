# LList_practice2_Nested_For_Loop_Remove.py
#
# author: Kaoru
# date: 14.09.23

# storing smaller chunk of list in a large list
# create an empty list, then append small lists
laptop_product = ["Laptop", 899.00, "USD", 2, 3.34, "Hardware"]
keyboard_product = ["Keyboard", 29.50, "USD", 6, 4.80, "Peripherals"]
mouse_product = ["Mouse", 13.99, "USD", 14, 2.45, "Peripherals"]

inventory_products = []
inventory_products.append(laptop_product)
inventory_products.append(keyboard_product)
inventory_products.append(mouse_product)

# looping through the larger outer list and print each individual list
for product_list in inventory_products:
    print(product_list)

# removing item
category = laptop_product[5]
laptop_product.remove(category)
print(laptop_product,
      inventory_products,
      )

