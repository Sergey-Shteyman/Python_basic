from garden import Garden
from gardener import Gardener


my_garden = Garden(5)
my_gardener = Gardener("Mihalich", my_garden)

while True:

    print(f"\n{my_gardener.name} должен по ухаживать за грядкой!")
    user_input = input(f"Отправить {my_gardener.name} полить картошку(да/нет)? ").lower()
    if user_input == "да":
        result = my_gardener.care_garden()
        if result:
            print(f"Отправляем {my_gardener.name} собирать урожай")
            print(f"Садовник {my_gardener.name} собрал {my_gardener.collect_potatos()} картошек)")
            print("Конец работы программы..")
            break
    else:
        my_garden.garden_life -= 1
        print(f"\nЕсли не поливать грядку, картошка может умереть!"
              f"\nОсталось жизней у картошки: {my_garden.garden_life}")
        if my_garden.garden_life == 0:
            print("Вся картошка пожухла(")
            break




