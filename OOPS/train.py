class train():
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getinfo(self):
        print(f"Train Name: {self.name}, Fare: {self.fare}, Seats: {self.seats}")
user=train("Express", 150, 100)
user.getinfo()  # Train Name: Express, Fare: 150, Seats:      