count_of_cards = int(input("Кол-во видеокарт: "))
lst_of_cards = []
new_lst_of_cards = []
for index in range(1, count_of_cards + 1):
    print(f"{index} Видеокарта: ", end='')
    lst_of_cards.append(int(input()))
max_series = max(lst_of_cards)
for series in lst_of_cards:
    if series < max_series:
        new_lst_of_cards.append(series)
print("\nСтарый список видеокарт:", lst_of_cards)
print("Новый список видеокарт:", new_lst_of_cards)
