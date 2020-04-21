from movements import ICrawling, IDigging
from .animal import Animal

class Gerbil(Animal, ICrawling, IDigging):
    def __init__(self, name):
        Animal.__init__(self, name)
        ICrawling.__init__(self)
        IDigging.__init__(self)

    def __str__(self):
        return f"This is {self.name} the gerbil!"

    def dig(self):
        print(f"{self.name} the gerbil is a digger.")

    def crawl(self):
        print(f"{self.name} the gerbil crawls.")