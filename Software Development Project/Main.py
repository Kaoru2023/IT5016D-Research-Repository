# Main.py
#
# author: Kaoru
# date: 09.09.23

# UPDATE & REVISION
# from Menu_Display.py, using Option2 to display menu
# consider using Option1 later stage
import Ticket


class Main:
    # to start thicket number from 2001
    ticket_counter = 2000
    all_tickets = []

    def print_menu(self):
        print("-----------------------------------",
              "Help Desk Ticketing System Menu:",
              "1. Submit New Ticket",
              "2. Show All Tickets",
              "3. Respond to Ticket by Number",
              "4. Reopen Closed Ticket",
              "5. Show Ticket Statistics",
              "6. Exit",
              "-----------------------------------",
              sep="\n"
              )

    # to make code CLEAR, define methods first and call them later
    def add_ticket(self):
        staff_id = input("Enter your staff ID: ")
        creator_name = input("Enter your name: ")
        contact_email = input("Enter contact Email: ")
        description = input("Enter description of issue. To change password, enter 'Password Change': ")
        self.ticket_counter += 1
        new_ticket = Ticket.Ticket(self.ticket_counter, staff_id, creator_name, contact_email, description)
        self.all_tickets.append(new_ticket)
        if "Password Change" in description:
            new_ticket.resolve_password_change()
            print(new_ticket.response)
            print(f"Ticket Number: {new_ticket.ticket_number}")
        else:
            print(f"Ticket Submitted Successfully! Ticket Number: {new_ticket.ticket_number}")
        self.show_ticket_stats()

    def show_all_tickets(self):
        for ticket in self.all_tickets:
            print("-----------------------------------")
            ticket.ticket_info()
            print("-----------------------------------")

    def respond_ticket(self):
        ticket_number = int(input("Enter Ticket Number to Respond: "))
        for ticket in self.all_tickets:
            if ticket.ticket_number == ticket_number and ticket.status == "Open":
                response = input("Enter Response: ")  # moved this from before if condition
                ticket.resolve_ticket(response)
                print("Response added to the ticket.")
                break
        else:
            print("Ticket not found or already closed.")

    def reopen_ticket(self):
        ticket_number = int(input("Enter Ticket Number to Reopen: "))
        for ticket in self.all_tickets:
            if ticket.ticket_number == ticket_number and ticket.status == "Closed":
                ticket.reopen_ticket()
                print("Ticket reopened.")
                break
        else:
            print("Ticket not found or not closed.")

    def show_ticket_stats(self):
        print("-----------------------------------")
        if self.ticket_counter < 2001:
            print("Submitted Tickets: 0",
                  "Resolved Tickets: 0",
                  "Open Tickets: 0",
                  sep="\n"
                  )
        else:
            ticket = self.all_tickets[0]
            ticket.ticket_stats()

    def exit(self):
        print("Goodbye!")

    def main(self):
        # to print the menu, use the infinite loop, then ask user to choose an option
        # to make the code clearer and easier to understand, use the function"print_menu"
        # to print the menu
        while True:
            self.print_menu()
            # to create ROBUST CODE, use EXCEPTION HANDLING
            try:
                option = int(input("Enter your choice 1 - 6: "))
            except ValueError:
                print("Wrong input. Please enter a number ...")
            # check what choice was entered and act accordingly
            else:
                if option == 1:
                    self.add_ticket()
                elif option == 2:
                    self.show_all_tickets()
                elif option == 3:
                    self.respond_ticket()
                elif option == 4:
                    self.reopen_ticket()
                elif option == 5:
                    self.show_ticket_stats()
                elif option == 6:
                    self.exit()
                    break
                else:
                    print("Invalid option. Please enter a number between 1 - 6.")


if __name__ != "__main__":
    pass
else:
    Main().main()
