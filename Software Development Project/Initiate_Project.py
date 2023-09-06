# Initiate_Project.py
#
# author: Kaoru
# date: 05.09.23
'''
class Ticket:
    ticket_count = 2001
    all_tickets = []

def __init__(self, ticket_number, staff_id, creator_name, email_address, issue_description):
    self.ticket_number = Ticket.ticket_count
    Ticket.ticket_count += 1
    self.staff_id = staff_id
    self.creator_name = creator_name
    self.email_address = email_address
    self.issue_description = issue_description
    self.response = "Not Yet Provided."
    self.status = "Open"

def submit_ticket(self):
    input()
'''
class Ticket:
    ticket_counter = 2001 # to start thicket number from 2001
    all_tickets = []

    def __init__(self, ticket_number, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.all_tickets.append(self)

    def submit_ticket(self):
        print(f"Ticket Submitted Successfully! Ticket Number: {self.ticket_number}")

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New Password: {new_password}"
        self.status = "Closed"

    def resolve_ticket(self, response):
        self.response = response
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def print_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator Name: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Contact Email: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}\n")

    @staticmethod
    def ticket_stats():
        total_tickets = len(Ticket.all_tickets)
        resolved_tickets = sum(1 for ticket in Ticket.all_tickets if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets
        return total_tickets, resolved_tickets, open_tickets


def display_menu():
    print("Help Desk Ticketing System Menu:")
    print("1. Submit a New Ticket")
    print("2. Respond to a Submitted Ticket")
    print("3. Reopen a Closed Ticket")
    print("4. Check Ticket Status")
    print("5. Display Ticket Information")
    print("6. Display Ticket Statistics")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            staff_id = input("Enter Staff ID: ")
            creator_name = input("Enter Ticket Creator Name: ")
            contact_email = input("Enter Contact Email: ")
            description = input("Enter Description of the Issue: ")
            new_ticket = Ticket(staff_id, creator_name, contact_email, description)
            new_ticket.submit_ticket()
            if "Password Change" in description:
                new_ticket.resolve_password_change()
                print(new_ticket.response)
        elif choice == "2":
            ticket_number = int(input("Enter Ticket Number to Respond: "))
            response = input("Enter Response: ")
            for ticket in Ticket.all_tickets:
                if ticket.ticket_number == ticket_number and ticket.status == "Open":
                    ticket.resolve_ticket(response)
                    print("Response added to the ticket.")
                    break
            else:
                print("Ticket not found or already closed.")
        elif choice == "3":
            ticket_number = int(input("Enter Ticket Number to Reopen: "))
            for ticket in Ticket.all_tickets:
                if ticket.ticket_number == ticket_number and ticket.status == "Closed":
                    ticket.reopen_ticket()
                    print("Ticket reopened.")
                    break
            else:
                print("Ticket not found or not closed.")
        elif choice == "4":
            ticket_number = int(input("Enter Ticket Number to Check Status: "))
            for ticket in Ticket.all_tickets:
                if ticket.ticket_number == ticket_number:
                    print(f"Ticket Status: {ticket.status}")
                    break
            else:
                print("Ticket not found.")
        elif choice == "5":
            ticket_number = int(input("Enter Ticket Number to Display Information: "))
            for ticket in Ticket.all_tickets:
                if ticket.ticket_number == ticket_number:
                    ticket.print_ticket_info()
                    break
            else:
                print("Ticket not found.")
        elif choice == "6":
            total, resolved, open = Ticket.ticket_stats()
            print(f"Total Tickets: {total}")
            print(f"Resolved Tickets: {resolved}")
            print(f"Open Tickets: {open}")
        elif choice == "7":
            print("Exiting the Help Desk Ticketing System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



