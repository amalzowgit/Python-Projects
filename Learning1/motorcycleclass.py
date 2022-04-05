# https://python.land/objects-and-classes/python-inheritance
# create motorcycle class, override init method

class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    def start(self):
        print("Sorry, out of fuel!")
        