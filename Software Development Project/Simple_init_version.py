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
