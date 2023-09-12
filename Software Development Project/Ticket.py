# Ticket.py
#
# author: Kaoru
# date: 12.09.23

# modify in conjunction with Main.py
# creating Ticket class to store all ticket information
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

    # to update the ticket’s response, change status to Closed,
    # increase the number of closed tickets and decrease the number of open tickets by 1.
    def resolve_password_change(self):
        new_password = self.get_generated_new_password()
        self.response = f"New Password Generated: {new_password}"
        self.status = "Closed"
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    # to generate the new password with:
    # The first two characters of the staffID, followed by the first three characters of the ticket creator name
    def get_generated_new_password(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        return new_password

    def ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}",
              f"Ticket Creator Name: {self.creator_name}",
              f"Staff ID: {self.staff_id}",
              f"Contact Email: {self.contact_email}",
              f"Description: {self.description}",
              f"Response: {self.response}",
              f"Status: {self.status}",
              sep="\n"
              )

    # Upon response to a ticket, change Ticket’s status to Closed,
    # increase the number of closed tickets and decrease the number of open tickets by 1.
    def resolve_ticket(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    # Upon reopen a ticket, change Ticket’s status to Reopened
    # increase the number of open tickets and decrease the number of closed tickets by 1.
    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.resolved_tickets -= 1
        Ticket.open_tickets += 1

    # Statistics:
    # The number of tickets submitted
    # The number of resolved tickets
    # The Number of open tickets
    # A way to display those statistics to the console.
    def get_ticket_stats(self):
        return [Ticket.open_tickets + Ticket.resolved_tickets,
                Ticket.resolved_tickets,
                Ticket.open_tickets]
