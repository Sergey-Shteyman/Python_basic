lst_count = int(input("Кол-во клеток: "))
effective_lst = []
inefficient_lst = []
for index in range(1, lst_count + 1):
    print(f"Эффеективность {index} клетки: ", end='')
    value = int(input())
    effective_lst.append(value)
    if value < index:
        inefficient_lst.append(value)
if len(inefficient_lst) != 0:
    print("Неподходящие значения: ", end='')
    for i in inefficient_lst:
        print(i, end=' ')
else:
    print("Все клетки подходят!")