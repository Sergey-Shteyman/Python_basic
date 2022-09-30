quantity_skates = int(input("Кол-во коньков: "))
lst_sizes_skates = []
for index in range(1, quantity_skates + 1):
    print(f"Размер {index}-й пары: ", end='')
    lst_sizes_skates.append(int(input()))
print("")
quantity_humans = int(input("Кол-во людей: "))
lst_sizes_humans = []
for index in range(1, quantity_humans + 1):
    print(f"Размер ноги {index}-го человека: ", end='')
    lst_sizes_humans.append(int(input()))
count_humans = 0
for size in lst_sizes_skates:
    if lst_sizes_humans.__contains__(size):
        count_humans += 1
        lst_sizes_humans.remove(size)
print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count_humans}")