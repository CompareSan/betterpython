import string
import random
from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

# Strategy pattern improve cohesion. 
class BaseProcessingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOProcessingStrategy(BaseProcessingStrategy):
    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        return tickets.copy()
    
class FILOProcessingStrategy(BaseProcessingStrategy):
    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        tickets_copy = tickets.copy()
        return tickets_copy.reverse()
            

class CustomerSupport:

    def __init__(self):
        self.tickets = []
        

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: BaseProcessingStrategy):
        tickets_list = processing_strategy.create_ordering(self.tickets)
        for ticket in tickets_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(FIFOProcessingStrategy())
