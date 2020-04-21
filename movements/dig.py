class IDigging:
    def __init__(self):
        self.dig_speed = 0
        self.depth = 0
        self.has_claws = True

    def dig(self):
        print("How the animal digs")