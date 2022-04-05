# https://python.land/objects-and-classes/python-inheritance
# redefine car class

class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False
