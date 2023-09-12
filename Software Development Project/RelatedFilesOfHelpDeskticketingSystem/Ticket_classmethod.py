# Initiate_Project.py
#
# author: Kaoru
# date: 10.09.23

from enum import auto, Enum


# modify in conjunction with Main.py
class Ticket:
    open_tickets = 0
    resolved_tickets = 0

    class Status(Enum):
        Open = auto()
        Closed = auto()
        Reopened = auto()

    @classmethod
    def get_ticket_stats(cls):
        return [Ticket.open_tickets, Ticket.resolved_tickets]

    def __init__(self, ticket_counter, staff_id, creator_name, contact_email, description):
        self.ticket_number = ticket_counter
        Ticket.open_tickets += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = Ticket.Status.Open

    def resolve_password_change(self):
        new_password = self.get_generated_new_password()
        self.response = f"New Password Generated: {new_password}"
        self.status = Ticket.Status.Closed
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    def get_generated_new_password(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        return new_password

    def get_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}", #include print here? or print in Main?
              f"Ticket Creator Name: {self.creator_name}",
              f"Staff ID: {self.staff_id}",
              f"Contact Email: {self.contact_email}",
              f"Description: {self.description}",
              f"Response: {self.response}",
              f"Status: {self.status.name}",
              sep="\n"
              )

    def resolve_ticket(self, response):
        self.response = response
        self.status = Ticket.Status.Closed
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    def reopen_ticket(self):
        self.status = Ticket.Status.Reopened
        Ticket.resolved_tickets -= 1
        Ticket.open_tickets += 1

    def ticket_stats(self):
        print(f"Submitted Tickets: {Ticket.open_tickets + Ticket.resolved_tickets}",
              f"Resolved Tickets: {Ticket.resolved_tickets}",
              f"Open Tickets: {Ticket.open_tickets}",
              sep="\n"
              )