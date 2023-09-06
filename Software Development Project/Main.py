# Main.py
#
# author: Kaoru
# date: 05.09.23

# from Menu_Display.py, using Option2 to display menu
class Main:
    def print_menu(self):
        print("1. Submit Ticket")
        print("2. Respond Ticket")
        print("3. Reopen Ticket")
        print("4. Exit")
    #print_menu1()

    # to make code CLEAR, define methods first and call them later
    def option1(self):
        print("Enter Staff ID")
    def option2(self):
        print("Enter Ticket Number")
    def option3(self):
        print("Enter Ticket Number")
    def option4(self):
        print("Goodbye")
    def main(self):
        # to print the menu, use the infinite loop, then ask user to choose an option
        # to make the code clearer and easier to understand, use the function"print_menu"
        #to print the menu
        while(True):
            self.print_menu()
            option = ""
            # to create ROBUST CODE, use EXCEPTION HANDLING
            try:
                option = int(input("Enter your choice: "))
            except:
                print("Wrong input. Please enter a number ...")
        # check what choice was entered and act accordingly
            if option == 1:
                self.option1()
            elif option == 2:
                self.option2()
            elif option == 3:
                self.option3()
            elif option == 4:
                self.option4()
                break
            else:
                print("Invalid option")

Main().main()

