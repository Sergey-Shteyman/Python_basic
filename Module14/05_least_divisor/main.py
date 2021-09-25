def n_d(num):
    """
    Находим наименьший делитель числа
    """
    lst = []
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            lst.append(i)
    if lst == []:
        return num
    else:
        return min(lst)


num = int(input("Введите число: "))
print(f"Наименьший делитель, отличный от единицы: {n_d(num)}")
