# Brain_Storm_Menu_Display.py
# # author: Kaoru
# date: 05.09.23

# OPTION 1 for print menu
# define a dictionary with the options
menu_options = {
    1: "Submit Ticket",
    2: "Respond ticket",
    3: "Reopen ticket",
    4: "Exit",
}
# print the dictionary to show the user the available options
def print_menu():
    for key in menu_options.keys():
        print(key, "--", menu_options[key])
#print_menu()



# OPTION 2 to print menu
def print_menu1():
    print("1. Submit Ticket")
    print("2. Respond Ticket")
    print("3. Reopen Ticket")
    print("4. Exit")

# to make code CLEAR, define methods first and call them later
def submitTicket():
    print("Enter Staff ID")
def option2():
    print("Enter Ticket Number")
def option3():
    print("Enter Ticket Number")
def option4():
    print("Goodbye")


# to print the menu, use the infinite loop, then ask user to choose an option
# to make the code clearer and easier to understand, use the function"print_menu"
#to print the menu
while(True):
    print_menu()
    option = ""
    # to create ROBUST CODE, use EXCEPTION HANDLING
    try:
        option = int(input("Enter your choice: "))
    except:
        print("Wrong input. Please enter a number ...")
# check what choice was entered and act accordingly
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
        break
    else:
        print("Invalid option")