count_list = int(input("Введите колличество элементов списка: "))
list_numbers = []
for i in range(1, count_list + 1):
    print(i, "элемент списка: ", end='')
    list_numbers.append(int(input()))

shift = int(input("Введите сдвиг: "))
shift_list = list_numbers[-shift:] + list_numbers[:-shift]
print("Изначальный список: ", list_numbers, sep='\n')
print("Сдвинутый список: ", shift_list)
