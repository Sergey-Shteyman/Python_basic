guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def guests_control(guests):
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    answer = input("Гость пришёл или ушёл? ")
    if answer != "Пора спать" and answer != "пора спать":
        if answer == "пришел":
            name = input("Имя гостя: ")
            if len(guests) < 6:
                print(f"Привет, {name}!")
                guests.append(name)
            else:
                print(f"Прости, {name}, но мест нет.")
        elif answer == "ушел":
            name = input("Имя гостя: ")
            print(f"Пока, {name}!")
            guests.pop(guests.index(name))
        guests_control(guests)
    else:
        print("\nВечеринка закончилась, все легли спать.")
        return


guests_control(guests)