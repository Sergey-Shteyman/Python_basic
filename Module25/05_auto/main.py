import math


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dist, angle):
        self.x = self.x + dist * math.cos(angle)
        self.y = self.y + dist * math.sin(angle)
        print('Едем к координатам', (round(self.x, 2), round(self.y, 2)), 'дальность пути: ', dist)

    def __str__(self):
        return f'Координаты машины ({round(self.x, 2)} {round(self.y, 2)})'


class Bus(Car):
    PAY_COEFF = 0.01
    MAX_PASSENGERS = 60

    def __init__(self, x, y):
        super().__init__(x, y)
        self.passengers = 0
        self.money = 0

    def move(self, distance, angle):
        if 0 < angle < 180:
            moneys = Bus.PAY_COEFF * self.passengers * distance
            self.money += Bus.PAY_COEFF * self.passengers * distance
            super().move(distance, angle)
            nord = 'Север'
            print(f'Автобус проехал {distance} км на {nord} и водитель заработал {moneys}')
        elif 180 < angle < 360:
            moneys = Bus.PAY_COEFF * self.passengers * distance
            self.money += Bus.PAY_COEFF * self.passengers * distance
            super().move(distance, angle)
            south = 'Юг'
            print(f'Автобус проехал {distance} км на {south} и водитель заработал {moneys}')
        else:
            print(f'Улетел в космос на {distance} км ')

    def enter(self, passengers):
        if self.passengers + passengers > Bus.MAX_PASSENGERS:
            print(f'Максимальная вместимость автобуса 60 (человек) из {passengers} желающих уехать')
            print(f'Сели в автобус только {Bus.MAX_PASSENGERS - self.passengers}')
            print(f'Не влезло в автобус {self.passengers + passengers - Bus.MAX_PASSENGERS}')
            self.passengers = Bus.MAX_PASSENGERS
        else:
            self.passengers += passengers
            print(f'В автобус сели {passengers} пассажиров')
        return self.passengers

    def exit(self, passengers):
        if self.passengers - passengers < 0:
            print('Все вышли из автобуса')
            self.passengers = 0
        else:
            self.passengers -= passengers
            print(f'Из автобуса вышли {passengers} осталось {self.passengers} пассажиров')
        return self.passengers

    def __str__(self):
        lines = [
            f'Координаты автобуса ({round(self.x, 2)} {round(self.y, 2)})',
            f'В автобусе {self.passengers} пассажиров',
            f'Водитель заработал {round(self.money, 2)} денег всего',
        ]
        return '\n'.join(lines)


bus = Bus(x=1, y=2)
bus.enter(50)
bus.move(40, 60)
bus.exit(20)
bus.move(20, 190)
bus.exit(20)
bus.enter(70)
bus.move(30, 400)
print(bus)
bus.exit(70)
print(bus)