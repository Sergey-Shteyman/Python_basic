count_of_cards = int(input("Кол-во видеокарт: "))
list_of_cards = []
new_list_of_cards = []
for i in range(1, count_of_cards + 1):
    print(f"{i} Видеокарта: ", end='')
    series = int(input())
    list_of_cards.append(series)
max_series = max(list_of_cards)
for i in list_of_cards:
    if i < max_series:
        new_list_of_cards.append(i)
print("\nСтарый список видеокарт:", list_of_cards)
print("Новый список видеокарт:", new_list_of_cards)
