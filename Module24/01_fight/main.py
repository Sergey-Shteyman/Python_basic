from warrior import Warrior
from random import randint


def war():
    first_warrior = Warrior("Македонский", 100, 20)
    second_warrior = Warrior("Наполеон", 100, 20)
    warriors = [first_warrior, second_warrior]

    print("Война началась\n")

    while True:
        warrior = randint(0, 1)
        target_enemy = (warrior + 1) % 2
        health_warrior = warriors[warrior].damage_give(warriors[target_enemy])
        if health_warrior == 0:
            print(f'Игра окончена!\n'
                  f'{warriors[warrior].name} победил!')
            break


war()


