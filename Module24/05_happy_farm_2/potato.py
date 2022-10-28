class Potato:
    states = {
        0: "Картошки пока нет",
        1: 'росток',
        2: "зеленая",
        3: "зрелая"
    }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.state_info()

    def state_info(self):
        print(f"Картошка {self.index} сейчас {self.states[self.state]}")

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False
