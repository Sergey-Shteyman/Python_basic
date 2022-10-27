class Human:
    def __init__(self, name, satiety=50, food=50, money=0):
        self.name = name
        self. satiety = satiety
        self.food = food
        self.money = money

    def day(self, action):
        if self.satiety < 20 and self.food >= 10:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} поел')
        elif self.food < 10 and self.money > 0:
            self.food += 20
            self.money -= 10
            print(f'{self.name} сходил в магазин')
        elif action == 1:
            self.money += 50
            print(f'{self.name} работает')
        elif action == 2:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} трапезничает')
        else:
            self.satiety -= 10
            print(f'{self.name} играет')

