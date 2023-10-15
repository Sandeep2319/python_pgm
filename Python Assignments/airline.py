
'''
Exercise 02 : Classes and objects -- try creating this in oops world
-------------------------------------------

Create a class that captures airline tickets. 
Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

main method:
Make two examples of tickets being sold to passengers.
display tickets booked details 
'''

class AirlineTicket:
    #intialize the value
    def __init__(self, departure_city,arrival_city,flight_number,seat_assignment):
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.flight_number = flight_number
        self.seat_assignment = seat_assignment

# Creating two examples of tickets being sold to passengers
ticket1 = AirlineTicket("New York", "London", "BA123", "12F")
ticket2 = AirlineTicket("Paris", "Tokyo", "AF456", "8B")

# Displaying ticket details
print("Ticket 1:")
print("Departure City:", ticket1.departure_city)
print("Arrival City:", ticket1.arrival_city)
print("Flight Number:", ticket1.flight_number)
print("Seat Assignment:", ticket1.seat_assignment)

print("\nTicket 2:")
print("Departure City:", ticket2.departure_city)
print("Arrival City:", ticket2.arrival_city)
print("Flight Number:", ticket2.flight_number)
print("Seat Assignment:", ticket2.seat_assignment)


