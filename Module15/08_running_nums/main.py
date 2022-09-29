count_list = int(input("Введите колличество элементов списка: "))
lst_numbers = []
for index in range(1, count_list + 1):
    print(index, "элемент списка: ", end='')
    lst_numbers.append(int(input()))

shift = int(input("Введите сдвиг: "))
shift_lst = lst_numbers[-shift:] + lst_numbers[:-shift]
print("Изначальный список: ", lst_numbers, sep='\n')
print("Сдвинутый список: ", shift_lst)
