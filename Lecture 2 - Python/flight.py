class Flight(): #defining a class called Flight
    def __init__(self, capacity): #defining the __init__ method, which is a special method that is called when an instance of the class is created. It takes one parameter, capacity, which is used to initialize the capacity attribute of the class. The passengers attribute is initialized as an empty list to store the names of passengers on the flight.
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name): #defining a method called add_passenger that takes a name as a parameter. This method checks if there are open seats on the flight by calling the open_seats method. If there are no open seats, it returns False. If there are open seats, it adds the name to the passengers list and returns True.
        if not self.open_seats(): #checking if there are open seats on the flight by calling the open_seats method. If the result is False (meaning there are no open seats), it
            return False #returning False to indicate that the passenger could not be added to the flight because it is full
        self.passengers.append(name) #adding the name of the passenger to the passengers list using the append method
        return True #returning True to indicate that the passenger was successfully added to the flight

    def open_seats(self): #defining a method called open_seats that calculates the number of open seats on the flight by subtracting the number of passengers from the capacity. It returns the number of open seats.
        return self.capacity - len(self.passengers) #calculating the number of open seats by subtracting the length of the passengers list (which gives the number of passengers currently on the flight) from the capacity attribute (which gives the total number of seats available on the flight). The result is returned as the number of open seats.
flight = Flight(4) #creating an instance of the Flight class called flight with a capacity of 4. This means that the flight can accommodate up to 4 passengers. The __init__ method is called when the instance is created, initializing the capacity attribute to 4 and the passengers attribute to an empty list.
people = ["Alice", "Bob", "Charlie", "Dessie", "Eve"]
for person in people: #iterating over the list of people using a for loop. For each person in the list, the loop will execute the block of code inside the loop.
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"Flight is full. {person} could not be added.")