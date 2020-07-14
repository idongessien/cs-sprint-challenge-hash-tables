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

    '''init array with the same number elements as tickets'''
    route = [None] * length
    
    '''traverse through tickets to save thier destination'''
    route_lookup = dict()

    '''traverse through tickets to save thier destination'''
    for ticket in tickets:
        
        route_lookup[ticket.source] = ticket.destination
    
    '''Starting ticket has source "NONE" '''
    next_destination = route_lookup["NONE"]

    '''get ticket new destination & add it to route array break when next destination is string "NONE"'''
    for current_leg in range(0, length):

        ''' get next destination '''
        route[current_leg] = next_destination        

        next_destination = route_lookup[next_destination]

    return route
