class HotelRoom:
    def __init__(self, room_number, capacity, rate):
        self.room_number = room_number
        self.capacity = capacity
        self.rate = rate
        self.occupants = []
        self.number_of_nights = 0
        self.total_charge = 0.00

    def check_in(self, name):
        self.occupants.append(name)

    def check_out(self):
        self.occupants = []

    def add_nights(self, nights):
        self.number_of_nights = nights
        self.total_charge = self.number_of_nights * self.rate
