# Main.py
#
# author: Kaoru
# date: 06.09.23

# UPDATE & REVISION
# from Menu_Display.py, using Option2 to display menu
# consider using Option1 later stage
import Ticket
class Main:
    def print_menu(self):
        print("Help Desk Ticketing System Menu:")
        print("1. Submit New Ticket")
        print("2. Show All Tickets")
        print("3. Respond to Ticket by Number")
        print("4. Reopen Closed Ticket")
        print("5. Show Ticket Statistics")
        print("6. Exit")

        # to make code CLEAR, define methods first and call them later
    def submit_ticket(self):
        staff_id = input("Enter Staff ID: ")
        creator_name = input("Enter Ticket Creator Name: ")
        contact_email = input("Enter Contact Email: ")
        description = input("Enter Description of the Issue. To change password, enter 'Password Change': ")
        new_ticket = Ticket.Ticket(staff_id, creator_name, contact_email, description)
        if "Password Change" in description:
            new_ticket.resolve_password_change()
            print(new_ticket.response, "\n",
                  f"Ticket Number: {new_ticket.ticket_number}")

        else:
            print(f"Ticket Submitted Successfully! Ticket Number: {new_ticket.ticket_number}")

    def respond_ticket(self):
        ticket_number = int(input("Enter Ticket Number to Respond: "))
        response = input("Enter Response: ")
        for ticket in Ticket.all_tickets:
            if ticket.ticket_number == ticket_number and ticket.status == "Open":
                ticket.resolve_ticket(response)
                print("Response added to the ticket.")
                break
        else:
            print("Ticket not found or already closed.")

    def reopen_ticket(self):
        ticket_number = int(input("Enter Ticket Number to Reopen: "))
        for ticket in Ticket.all_tickets:
            if ticket.ticket_number == ticket_number and ticket.status == "Closed":
                ticket.reopen_ticket()
                print("Ticket reopened.")
                break
        else:
            print("Ticket not found or not closed.")

    def ticket_information(self):
        print("AAAAAAAA")

    def ticket_status(self):
        ticket_number = int(input("Enter Ticket Number to Check Status: "))
        for ticket in Ticket.all_tickets:
            if ticket.ticket_number == ticket_number:
                print(f"Ticket Status: {ticket.status}")
                break
        else:
            print("Ticket not found.")

    def ticket_statistic(self):
        print("UUUUUUUUU")

    def main(self):
        # to print the menu, use the infinite loop, then ask user to choose an option
        # to make the code clearer and easier to understand, use the function"print_menu"
        #to print the menu
        while(True):
            self.print_menu()
            option = ""
            # to create ROBUST CODE, use EXCEPTION HANDLING
            try:
                option = int(input("Enter your choice 1 - 6: "))
            except:
                print("Wrong input. Please enter a number ...")
        # check what choice was entered and act accordingly
            if option == 1:
                self.submit_ticket()
            elif option == 2:
                self.option2()
            elif option == 3:
                self.option3()
            elif option == 4:
                self.option4()
                break
            else:
                print("Invalid option")

if __name__ == "__main__":
    Main().main()
