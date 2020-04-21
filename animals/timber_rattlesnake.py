from .animal import Animal
from movements import IDigging

class Timber_Rattlesnake(Animal, IDigging):
    def __init__(self, name):
        Animal.__init__(self, name)
        IDigging.__init__(self)

    def __str__(self):
        return f"This is a poisonous Timber Rattlesnake named {self.name}!"

    def dig(self):
        print(f"{self.name} the Timber Rattlesnake digs.")