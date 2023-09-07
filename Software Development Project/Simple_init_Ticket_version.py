# Simple_init_version.py
#
# author: Kaoru
# date: 06.09.23

class Ticket:
    ticket_counter = 2001
    all_tickets = []

    def __init__(self):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = None
        self.creator_name = None
        self.email = None
        self.description = None
        self.response = "Not Yet provided"
        self.status = "Open"
        Ticket.all_tickets.append(self)

    def submit_Ticket(self):
        print(f"Ticket Submitted Successfully! Ticket Number: {self.ticket_number}")

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New Password Generated: {new_password}"
        self.status = "Closed"

    def resolve_ticket(self, response):
        self.response = response
        self.status = "Closed"

    def

    def reopen_ticket(self):
        self.status = "Reopened"
