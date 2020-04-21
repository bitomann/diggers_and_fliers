from movements import ICrawling
from .animal import Animal

class Ant(Animal, ICrawling):
    def __init__(self, name):
        Animal.__init__(self, name)
        ICrawling.__init__(self)

    def __str__(self):
        return f"This is {self.name} the Ant."

    def walk(self):
        print(f"{self.name} the ant walks on six legs.")