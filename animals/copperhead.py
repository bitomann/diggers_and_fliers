from .animal import Animal
from movements import IDigging

class Copperhead(Animal, IDigging):
    def __init__(self, name):
        Animal.__init__(self, name)
        IDigging.__init__(self)

    def __str__(self):
        return f"This is {self.name} the Copperhead!"

    def dig(self):
        print(f"{self.name} the Copperhead is a digger.")