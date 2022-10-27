class Warrior:

    def __init__(self, name, health, punch):
        self.name = name
        self.health = health
        self.punch = punch

    def damage_give(self, enemy):
        if isinstance(enemy, Warrior):
            enemy.health -= self.punch
        if enemy.health > 0:
            print(f"{self.name} атаковал {enemy.name}\n"
                  f"{enemy.name} осталось {enemy.health} здоровья\n")
        else:
            print(f"{self.name} атаковал {enemy.name}\n"
                  f"{enemy.name} убит\n")

        return enemy.health