len_lst = int(input("Введите колличество элементов списка: "))
lst = []
for i in range(1, len_lst + 1):
    print(i, "элемент списка: ", end="")
    lst.append(int(input()))
print(f"Изначальный список: {lst}")

for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst [j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(f"Отсортированный список: {lst}")
