# You've booked a _really_ cheap one-way flight. Unfortunately, that means
# you have _tons_ of layovers before you reach your destination. The
# morning of, you woke up late and had to scramble to the airport to catch
# your first flight. However, in your rush, you accidentally scrambled all
# your flight tickets. You don't know the route of your entire trip now!

# Write a function `reconstruct_trip` to reconstruct your trip from your
# mass of flight tickets. Each ticket is represented as a class with the
# following form:

# ```
# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination
# ```

# where the `source` string represents the starting airport and the
# `destination` string represents the next airport along our trip. The
# ticket for your first flight has a destination with a `source` of
# `NONE`, and the ticket for your final flight has a `source` with a
# `destination` of `NONE`. 

# Pseudocode for an array of `Tickets` might look like this:

# ```
# tickets = [
#     Ticket{ source: "PIT", destination: "ORD" },
#     Ticket{ source: "XNA", destination: "CID" },
#     Ticket{ source: "SFO", destination: "BHM" },
#     Ticket{ source: "FLG", destination: "XNA" },
#     Ticket{ source: "NONE", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "CID", destination: "SLC" },
#     Ticket{ source: "ORD", destination: "NONE" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "BHM", destination: "FLG" }
# ]
# ```

# Your function should output an array of strings with the entire route of
# your trip. For the above example, it should look like this:

# ```
# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
# ```

# Your solution should run in linear time. You can assume that your
# function will always be handed a valid ticket chain as input. 

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
    ticket_table = {}
    route = []

    for ticket in tickets:
        if ticket.source not in ticket_table:
            ticket_table[ticket.source] = ticket.destination

    route.append(ticket_table["NONE"])   

    current_destination = route[0]    

    while current_destination != "NONE":
        current_destination = ticket_table[current_destination]
        route.append(current_destination)


    return route

