quantity_numbers = int(input("Кол-во чисел: "))
lst_numbers = []
for _ in range(quantity_numbers):
    # print("Число: ", end='')
    lst_numbers.append(int(input("Число: ")))
print(f"\nПоследовательность: {lst_numbers}")
counter = 0
while lst_numbers != lst_numbers[::-1]:
    lst_numbers.insert(quantity_numbers, lst_numbers[counter])
    counter += 1

print('Нужно приписать чисел:', counter)
print('Сами числа:', lst_numbers[:counter][::-1])