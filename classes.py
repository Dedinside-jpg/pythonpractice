class Order:
    def __init__(self, weight, place):
        self.weight = weight
        self.place = place

    def GetWeight(self):
        with open("weight.txt") as file:
            w_array = [row.strip() for row in file]
            return w_array

    def GetPlace(self):
        with open("places.txt") as file:
            p_array = [row.strip() for row in file]
            return p_array


class Courier:
    def __init__(self, capacity, place):
        self.place = place
        self.capacity = capacity




