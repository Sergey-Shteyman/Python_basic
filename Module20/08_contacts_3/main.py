def user_answer():
    print("\nВыберете вариант:")
    print(" 1. Добавить контакт",
          " 2. Найти человека",
          " 3. Выйти из поиска", sep='\n')
    user_input = input("Введите цифру действия: ")
    if user_input == '1':
        name_person = input(
            "Введите имя и фамилию нового контакта (через пробел): "
        ).split(" ")
        phone_number = input("Введите номер телефона: ")
        add_contact(name_person, phone_number)
    elif user_input == '2':
        name_person = input("Введите фамилию для поиска: ")
        finde_person(name_person)
    elif user_input == '3':
        print("\nКонец работы программы.")
        return
    else:
        print("\nНекорректный ввод!")
        user_answer()


def add_contact(name_person, phone_number):
    for key in all_contacts.keys():
        if (name_person[0].lower(), name_person[1].lower()) == (key[0].lower(), key[1].lower()):
            print("Такой человек уже есть в контактах.")
            print(f"Текущий словарь контактов: "
                  f"{all_contacts}")
            user_answer()

    all_contacts[tuple(name_person)] = phone_number
    print(f"Текущий словарь контактов: "
          f"{all_contacts}")
    user_answer()
    return


def finde_person(name_person):
    for key, value in all_contacts.items():
        if name_person.lower() == key[1].lower():
            print(*key, value)
    user_answer()
    return


all_contacts = {('Иван', 'Сидоров'): 888}
user_answer()


