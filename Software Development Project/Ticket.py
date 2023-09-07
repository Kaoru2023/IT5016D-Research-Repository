# Initiate_Project.py
#
# author: Kaoru
# date: 07.09.23

# modify in conjunction with Main.py
class Ticket:
    open_tickets = 0
    resolved_tickets = 0

    def __init__(self, ticket_counter, staff_id, creator_name, contact_email, description):
        self.ticket_number = ticket_counter
        Ticket.open_tickets += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def resolve_password_change(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New Password Generated: {new_password}"
        self.status = "Closed"
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    def ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator Name: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Contact Email: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}")  # removed new line

    def resolve_ticket(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.resolved_tickets -= 1
        Ticket.open_tickets += 1

    def ticket_stats(self):
        print(f"Submitted Tickets: {Ticket.open_tickets + Ticket.resolved_tickets}")
        print(f"Resolved Tickets: {Ticket.resolved_tickets}")
        print(f"Open Tickets: {Ticket.open_tickets}" )