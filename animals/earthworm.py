from .animal import Animal
from movements import IDigging

class Earthworm(Animal, IDigging):
    def __init__(self, name):
        Animal.__init__(self, name)
        IDigging.__init__(self)

    def __str__(self):
        return f"This is {self.name} the earthworm."

    def dig(self):
        print(f"{self.name} the earthworm is a digger.")