class Subterranean:
    def __init__(self, name):
        self.name = name
        self.animals = set()

    def add_animal(self, animal):
        if animal.dig_speed > -1:
            self.animals.add(animal)
        else:
            print(f"This animal will not survive in this environment")