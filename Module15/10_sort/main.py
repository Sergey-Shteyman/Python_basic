len_lst = int(input("Введите колличество элементов списка: "))
lst = []
for index in range(1, len_lst + 1):
    print(index, "элемент списка: ", end="")
    lst.append(int(input()))
print(f"Изначальный список: {lst}", end='\n')

for step in range(len(lst) - 1):
    for index in range(len(lst) - 1 - step):
        if lst[index] > lst[index + 1]:
            lst[index], lst[index + 1] = lst[index + 1], lst[index]

print(f"Отсортированный список: {lst}")