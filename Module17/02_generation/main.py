length = int(input("Введите длину списка: "))
special_generation = [1 if index % 2 == 0 else index % 5 for index in range(length)]
print(special_generation)
