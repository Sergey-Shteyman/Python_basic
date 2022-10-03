length_lst = int(input("Введите длину списка: "))
special_lst = [1 if index % 2 == 0 else index % 5 for index in range(length_lst)]
print(special_lst)
