# Tuple_more _Learning.py
#
# author: Kaoru
# date: 22.08.23


bank_accounts = (("Goro", 500, "135 Newton Road", "0120000133"),
                 ("Taro", 1000),
                 ("Hanako", 3600, "48 Konini Road"),
                 ("Kana", -95))

print("The number of bank accounts is ", len(bank_accounts))

# showing names and balances
# tried concatenation to remove space after $, but raised error saying str + int
# is invalid. So used .format() 
for i in bank_accounts:
    print("\nThe name is ", i[0], "and the balance is ${}".format(i[1]))

# showing only names and addresses
for i in bank_accounts:
    if len(i) > 2:
        print("\nThe name is ", i[0], "and the address is", i[2])

# Some account holders have more
# information than others. The additional information can be accessed without
# raising an error, by checking the length of each tuple before printing the
# information.

