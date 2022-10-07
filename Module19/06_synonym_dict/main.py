def get_key(dictionary, value):
    for keys, values in dictionary.items():
        if values == value:
            return keys


def finde_synonyms(synonyms):
    user_input = input("Введите слово: ").lower()
    if user_input in synonyms.values():
        print(f"Синоним: {get_key(synonyms, user_input)}")
        return
    else:
        print("Такого слова в словаре нет.")
        finde_synonyms(synonyms)


def get_pairs():
    global index
    quantity_pairs = int(input("Введите количество пар слов: "))
    synonyms = dict()
    for index in range(1, quantity_pairs + 1):
        pair = input(f"{index} пара: ").lower().split(" - ")
        synonyms[pair[0]] = pair[1]
    finde_synonyms(synonyms)


get_pairs()
# Привет - Здравствуйте
# Печально - Грустно