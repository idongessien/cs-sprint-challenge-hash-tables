#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # init array... 
    route = [None] * length

    # init dict...
    route_lookup = dict()

    # go through tickets...
    for ticket in tickets:

        # save destination...
        route_lookup[ticket.source] = ticket.destination

    # First ticket source none...
    next_destination = route_lookup["NONE"]

    # for each leg in route...
    for current_leg in range(0, length):

        # set leg to next destination...
        route[current_leg] = next_destination        
        
        # set next destination...
        next_destination = route_lookup[next_destination]

    return route
