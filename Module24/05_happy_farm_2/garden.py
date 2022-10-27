from potato import Potato


class Garden:

    garden_life = 3

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print("Картошка еще не созрела")
            return False
        else:
            print("Вся картошка созрела, можно собирать урожай")
            return True
