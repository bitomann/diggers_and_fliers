from movements import ISwimming
from .animal import Animal

class Betta_Fish(Animal, ISwimming):
    def __init__(self, name):
        Animal.__init__(self, name)
        ISwimming.__init__(self)

    def __str__(self):
        return f"This is {self.name} the betta fish."

    def swim(self):
        print(f"{self.name} the betta fish is a swimmer.")