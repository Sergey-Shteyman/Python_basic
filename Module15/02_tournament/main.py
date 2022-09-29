len_lst = int(input("Введите колличество элементов списка: "))
names = []
crew = []
for index in range(1, len_lst + 1):
    print(index, "элемент списка: ", end="")
    names.append(input())
print(f"Изначальный список: {names}")
for index in range(0, len(names)):
    if index % 2 == 0:
        crew.append(names[index])
print(f"Первый день {crew}")