number = int(input("Введите целое число N: "))
lst = []
for digit in range(1, number + 1):
    if digit % 2 != 0:
        lst.append(digit)
print(f"Список из нечетных чисел от 1 до {number}:  {lst}" )
