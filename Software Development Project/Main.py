# Main.py
#
# author: Kaoru
# date: 12.09.23

# import Ticket to use data stored in Ticket.py
from Ticket import Ticket


# creating Main class to store and use information in Ticket.py
class Main:
    ticket_counter = 2000
    all_tickets = {}

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

    # to make code CLEAR, define methods first and call them upon user's menu selection

    # for user to input when submitting ticket
    def add_ticket(self):
        staff_id = input("Enter your staff ID: ")
        creator_name = input("Enter your name: ")
        contact_email = input("Enter contact Email: ")
        description = input("Enter description of issue. To change password, enter 'Password Change': ")
        # to assign thicket number to new ticket, starting from 2001
        self.ticket_counter += 1
        new_ticket = Ticket(self.ticket_counter, staff_id, creator_name, contact_email, description)
        # to add and store new tickets in dictionary
        self.all_tickets[new_ticket.ticket_number] = new_ticket
        if "Password Change" in description:
            new_ticket.resolve_password_change()
            print(new_ticket.response)
            print(f"Ticket Number: {new_ticket.ticket_number}")
        else:
            print("Ticket Submitted Successfully!",
                  f"Ticket Number: {new_ticket.ticket_number}",
                  sep="\n"
                  )

        # to display stats after submitting ticket
        self.show_ticket_stats()

    # to display all tickets
    def show_all_tickets(self):
        if len(self.all_tickets) > 0:
            for ticket in self.all_tickets.values():
                print("-----------------------------------")
                ticket.ticket_info()
                print("-----------------------------------")
        else:
            print("No Tickets to show")

    # exception handling to respond open and existing ticket
    def respond_ticket(self):
        try:
            ticket_number = int(input("Enter Ticket Number to Respond: "))
            ticket = self.all_tickets[ticket_number]
            if (ticket.ticket_number == ticket_number
                and (ticket.status == "Open" or ticket.status == "Reopened")):
                response = input("Enter Response: ")  # moved this from before if condition
                ticket.resolve_ticket(response)
                print("Response added to the ticket.")
            else:
                print("Ticket not found or already closed.")
        except ValueError:
            print("Wrong input. Please enter a number ... ")
        except KeyError:
            print("Ticket number not found. Please check again.")

    def reopen_ticket(self):
        try:
            ticket_number = int(input("Enter Ticket Number to Reopen: "))
            ticket = self.all_tickets[ticket_number]
            if ticket.ticket_number == ticket_number and ticket.status == "Closed":
                ticket.reopen_ticket()
                print("Ticket reopened.")
            else:
                print("Ticket not found or not closed.")
        except ValueError:
            print("Wrong input. Please enter a number ... ")
        except KeyError:
            print("Ticket number not found. Please check again.")

    def show_ticket_stats(self):
        print("-----------------------------------")
        stats = [0, 0, 0]
        if self.ticket_counter > 2000:
            ticket = self.all_tickets[2001]
            stats = ticket.get_ticket_stats()
        print(f"Submitted Tickets: {stats[0]}",
              f"Resolved Tickets: {stats[1]}",
              f"Open Tickets: {stats[2]}",
              sep="\n"
              )

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
