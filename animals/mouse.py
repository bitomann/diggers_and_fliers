from movements import ICrawling, IDigging
from .animal import Animal

class Mouse(Animal, ICrawling, IDigging):
    def __init__(self, name):
        Animal.__init__(self, name)
        ICrawling.__init__(self)
        IDigging.__init__(self)

    def __str__(self):
        return f"This is {self.name} the mouse."

    def dig(self):
        print(f"{self.name} the mouse digs.")

    def walk(self):
        print(f"{self.name} the mouse crawls.")