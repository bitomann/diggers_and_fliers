class Sky:
    def __init__(self, name):
        self.name = name
        self.animals = set()

    def addAnimal(self, animal):
        if animal.altitude > -1:
            self.animals.add(animal)
        else:
            print(f"This animal will not survive in this environment")