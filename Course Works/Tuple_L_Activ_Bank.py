# Tuple_L_Activ_Bank.py
#
# authod: Kaoru
# date: 22.08.23


bank_accounts = (("Goro", 50, "135 Newton Road", "0120000133"),
                 ("Taro", 1000),
                 ("Hanako", 3600, "48 Konini Road"),
                 ("Kana", -95))


#The names of all customers with less than $100
for bankaccount in bank_accounts:
    if bankaccount[1] < 100:
       print("The name with the balance less than $100 is", bankaccount[0])
    

#The names of customers with no address and no phone number
for bankaccount in bank_accounts:
    if len(bankaccount) <= 2:
       print("The name without address is", bankaccount[0])

#The highest and lowest balances
max_balance = int()
min_balance = int()
for index,i in enumerate(bank_accounts):
#    print(index, i[1])
    if index == 0:
        max_balance = i[1]
        min_balance = i[1]
    elif max_balance < i[1]:
        max_balance = i[1]
    elif min_balance > i[1]:
        min_balance = i[1]
print("The hignest balance is ${}".format(max_balance))
print("The lowest balance is ${}".format(min_balance))
        
        
        


'''
Then sum of balances from all customers

Write code that prints all the details, for all the customers.
HINT: This will use a nested for statement to print each tuple

The full details for customers with more than $5000 or customers who are overdrawn
'''
