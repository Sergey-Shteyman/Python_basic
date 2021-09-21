def summ_digits(num):
    summ = 0
    while num != 0:
        summ += num % 10
        num //= 10
    return summ


def count_digits(num):
    count_d = 0
    while num != 0:
        count_d += 1
        num //= 10
    return count_d


num = int(input("Введите число: "))
summ = summ_digits(num)
count_d = count_digits(num)
print('-' * 20)
print()
print(f"Сумма цифр: {summ}",
      f"Кол-во цифр в числе: {count_d}",
      f"Разность суммы и кол-ва цифр: {summ - count_d}",
      sep='\n'
      )
