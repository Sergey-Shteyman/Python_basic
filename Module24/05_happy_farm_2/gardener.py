class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def care_garden(self):
        self.garden.grow_all()
        return self.garden.are_all_ripe()

    def collect_potatos(self):
        return len([potato for potato in self.garden.potatoes if potato.is_ripe()])