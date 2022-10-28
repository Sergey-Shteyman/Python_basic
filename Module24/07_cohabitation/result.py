from random import randint
from human import Human


class Result:
    def __init__(self, man_1, man_2):
        self.man_1 = man_1
        self.man_2 = man_2

    def life_death(self):
        if self.man_1.satiety == 0 or self.man_2.satiety == 0:
            print('Один из участников умер.')
            return True


human_1 = Human('Степан')
human_2 = Human('Артём')

result = Result(human_1, human_2)
count_day = 0

while True:
    count_day += 1
    if count_day == 365:
        print('\nЭксперимент удался. Все живы.')
        break
    elif result.life_death():
        break
    else:
        r = randint(1, 6)
        human_1.day(r)
        human_2.day(r)

print(count_day)
