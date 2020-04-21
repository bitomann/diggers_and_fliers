from movements import IFlying
from .animal import Animal

class Parakeet(Animal, IFlying):
    def __init__(self, name):
        Animal.__init__(self, name)
        IFlying.__init__(self)

    def __str__(self):
        return f"This is {self.name} the parakeet."

    def fly(self):
        print(f"{self.name} the parakeet flies.")