# Day 12 - Customer Support Ticket System
# Focus: Queue
# Language: Python 3

from collections import deque


class TicketSystem:
    def __init__(self):
        self.queue = deque()
        self.ticket_id = 1

    def create_ticket(self, customer_name, issue):
        ticket = {
            "id": self.ticket_id,
            "customer": customer_name,
            "issue": issue
        }
        self.queue.append(ticket)
        self.ticket_id += 1
        print(f"Ticket created: {ticket}")

    def resolve_ticket(self):
        if not self.queue:
            print("No tickets to resolve.")
            return None

        ticket = self.queue.popleft()
        print(f"Resolved ticket: {ticket}")
        return ticket

    def view_pending_tickets(self):
        if not self.queue:
            print("No pending tickets.")
            return

        print("\nPending Tickets:")
        for ticket in self.queue:
            print(ticket)


def main():
    system = TicketSystem()

    system.create_ticket("Alice", "Login issue")
    system.create_ticket("Bob", "Payment failed")
    system.create_ticket("Charlie", "App crash")

    system.view_pending_tickets()

    system.resolve_ticket()
    system.resolve_ticket()

    system.view_pending_tickets()


if __name__ == "__main__":
    main()
