# Split_For_loop_Casting.py
#
# author: Kaoru
# date: 14.09.23

# splits the receipts string into a list of strings using the comma as the delimiter
receipts = "67.88,99.34,23.45,39.09"
receipt_list = receipts.split(",")
# initializes a variable total_sales to 0
total_sales = 0
# loops through each string in the receipt_list
for purchase in receipt_list:
    price_float = float(purchase)  # convert each string to a float
    price_float += total_sales   # add to the total_sales variable
print(total_sales)  # print the total sum of all the prices in the receipt_list. 229.76