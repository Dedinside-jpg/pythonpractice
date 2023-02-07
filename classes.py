class Order(object):
    def __init__(self, weight, place):
        self.weight = weight
        self.place = place

    def GetWeight(self):
        with open("weight.txt") as file:
            warray = [row.strip() for row in file]
            return warray

    def GetPlace(self):
        with open("places.txt") as file:
            parray = [row.strip() for row in file]
            return parray


class Courier(object):
    def __init__(self, place, capacity):
        self.place = place
        self.capacity = capacity




