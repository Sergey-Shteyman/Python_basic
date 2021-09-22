def reversed_number(num):
    num = str(num).split('.')
    reversed_num = [''.join(reversed(i)) for i in num]
    return float('.'.join(reversed_num))


num_1 = reversed_number(float(input("Введите число: ")))
num_2 = reversed_number(float(input("Введите второе число: ")))
print()
print(f"Первое число наоборот: {num_1}",
      f"Второе число наоборот: {num_2}",
      f"Сумма: {num_1 + num_2}",
      sep="\n")


