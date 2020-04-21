from .animal import Animal
from movements import ICrawling, ISwimming, IDigging

class Terrapin(Animal, ICrawling, ISwimming, IDigging):
    def __init__(self, name):
        Animal.__init__(self, name)
        ICrawling.__init__(self)
        ISwimming.__init__(self)
        IDigging.__init__(self)

    def __str__(self):
        return f"This is {self.name} the terrapin."

    def crawl(self):
        print(f"{self.name} the terrapin crawls.")

    def swim(self):
        print(f"{self.name} the terrapin swims.")

    def dig(self):
        print(f"{self.name} the terrapin digs.")